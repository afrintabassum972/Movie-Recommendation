# 🎬 Movie Recommendation System

Yeh ek **Machine Learning** based web application hai jo aapki pasandida movie ke adhaar par top 5 similar movies recommend karta hai. Ismein **TMDB API** ka upyog karke real-time posters bhi dikhaye jate hain.

## 🚀 Features
*   **Interactive UI:** Streamlit ka upyog karke ek saaf aur asaan interface.
*   **Top 5 Recommendations:** Kisi bhi movie ko select karne par usse milti-julti movies dikhata hai.
*   **Real-time Posters:** Movies ke saath unke official posters bhi fetch karta hai.

## 🛠️ Tech Stack
*   **Language:** Python
*   **Framework:** [Streamlit](https://streamlit.io)
*   **Libraries:** Pandas, Requests, Pickle, Scikit-learn
*   **API:** [TMDB Movie API](https://themoviedb.org)

## 📂 Project Structure
```text
├── app.py                # Main application code (Streamlit)
├── movie_dict.pkl        # Processed movies data (Dictionary)
├── similarity.pkl        # Precomputed similarity matrix
├── requirements.txt      # List of dependencies
├── tmdb_5000_movies.csv  # Original Dataset (Movies)
├── tmdb_5000_credits.7z  # Original Dataset (Credits)
└── README.md             # Project documentation

