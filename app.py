import streamlit as st
import pickle
import numpy as np
import requests

movies = pickle.load(open('model/movies.pkl','rb'))

similarity = pickle.load(open('model/similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommended_movies_index = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])
    recommended_movies = []
    recommended_movie_posters = []
    for i in recommended_movies_index[1:no_of_recommendations+1]:
        movie_id = movies.iloc[i[0]].movie_id       
        recommended_movie_posters.append(fetch_poster(movie_id))                                                                                         
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies,recommended_movie_posters    


st.title('Movie Recommender System')

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values,
)

options = ["5", "10", "15", "20"]

selection = st.segmented_control(
    "Select number of Recommendations:",
    options=options,
    selection_mode="single",
    default=options[0]  
)
no_of_recommendations = int(selection)



recommend_movies = st.button('Recommend')

if recommend_movies:
    names,posters = recommend(selected_movie)

    for i in range(0,no_of_recommendations, 5):
        cols = st.columns(5)
        for j, col in enumerate(cols):
                with col:
                    st.text(names[i + j])
                    st.image(posters[i + j])