# Movie Recommender System

A web app that recommends movies based on your selection, showing movie titles and posters.

##  Live Demo
[Movie Recommender System](https://movie-recommender-system-ml1.streamlit.app)

##  Built With
- **Python**  
- **Streamlit** (for UI)  
- **Pandas & NumPy** (data handling)  
- **Pickle** (model serialization)  
- **Git LFS** (for large model files)

## 📂 Project Structure
movie_recommender_system/  
│
├── app.py   
├── requirements.txt    
├── .gitignore  
├── data/   
│ ├── tmdb_5000_credits.csv  
│ ├── tmdb_5000_movies.csv  
│ └── movie_recommender_system.ipynb  
└── model/   
├── movies.pkl  
└── similarity.pkl  



---

## **How to Run Locally**

**Clone the repository:**
```bash
git clone https://github.com/Joti-Sukheja/movie_recommender_system.git
cd movie_recommender_system
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the app::**
```bash
streamlit run app.py
```


## **Features**

- Select a movie from the dropdown.
- Choose number of recommendations.
- Get recommended movies with posters.

---


