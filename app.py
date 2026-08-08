import streamlit as st
import pickle
import pandas as pd
import requests
import time

session = requests.session()
session.headers.update({"user_Agent": "MovieApp/1.0"})

def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": api_key,
        "language": "en-US"
    }
    for attempt in range(3):
        try:
            response = session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path', None)
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                return "https://placeholder.com"
        except requests.exceptions.RequestException:
            if attempt < 2:
                time.sleep(1)
                continue
            return "https://placeholder.com"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open("similarity.pkl", 'rb'))

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Enter the name of a movie",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.markdown(f"<p style='text-align: center; font-weight: bold;'>{names[i]}</p>", unsafe_allow_html=True)
