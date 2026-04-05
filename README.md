# Movie Recommendation System 🎬

Ek machine learning based web application jo aapki pasandida movie ke basis par top 5 similar movies recommend karti hai. Ismein **Content-Based Filtering** ka use kiya gaya hai aur UI ke liye **Streamlit** ka istemal hua hai.

## ✨ Features
*   **User-friendly Interface:** Streamlit ka upyog karke banaya gaya simple clean UI.
*   **Accurate Recommendations:** Movie metadata ka use karke similar movies find karta hai.
*   **Dynamic Posters:** TMDB API ka use karke real-time mein movie posters fetch karta hai.

## 🛠️ Tech Stack
*   **Language:** Python
*   **Libraries:** Pandas, Scikit-learn, Streamlit, Requests, Pickle
*   **API:** [The Movie Database (TMDB)](https://themoviedb.org)

## 📁 Project Structure
```text
├── app.py                # Main Streamlit application code
├── movie_dict.pkl        # Processed movie data dictionary
├── similarity.pkl        # Cosine similarity matrix
└── README.md             # Project documentation

## ⚙️ Setup Instruction

1. **Dependencies Install Karein:**
   Apne terminal ya command prompt mein niche di gayi command chalaein:
   ```bash
   pip install streamlit pandas requests
2. **API Key Setup:**
   Apni TMDB API Key ko `.streamlit/secrets.toml` file mein is tarah likhein:
   ```toml
   TMDB_API_KEY = "aapki_api_key_yahan_daalein"
3. **App Run Karein:**
   Project folder mein jaakar terminal mein likhein:
   ```bash
   streamlit run app.py

## 🧠 How it Works?
Jab aap koi movie select karte hain, toh system `similarity.pkl` file ka use karke us movie ke vectors aur baaki movies ke vectors ke beech ka **Cosine Similarity** (distance) nikaalta hai aur sabse kareebi 5 movies ko unke posters ke sath display karta hai.

---
**Developed by [Afrin Tabassum]**
