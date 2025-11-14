import streamlit as st
import pickle
import requests

# ============================
# Load Model & Data
# ============================
movies = pickle.load(open('model/movies.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))


# ============================
# Fetch Movie Poster
# ============================
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url).json()
        poster_path = response.get('poster_path', None)
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=No+Image"


# ============================
# Recommendation Function
# ============================
def recommend(movie, top_n):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    sorted_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_posters = []

    for i in sorted_list[1:top_n+1]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# ============================
# UI Styling
# ============================
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 42px !important;
        font-weight: 700;
        padding: 10px;
        background: linear-gradient(to right, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .movie-card {
        padding: 10px;
        border-radius: 12px;
        background-color: #1f1f1f;
        box-shadow: 0px 0px 6px rgba(255,255,255,0.1);
        transition: 0.3s;
    }
    .movie-card:hover {
        transform: scale(1.03);
        box-shadow: 0px 0px 12px rgba(255,255,255,0.2);
    }
    .footer {
        text-align:center;
        margin-top:50px;
        opacity:0.7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================
# Header
# ============================
st.markdown('<h1 class="main-title">🎬 Movie Recommender System</h1>', unsafe_allow_html=True)
st.write("### Discover movies similar to your favorites")


# ============================
# Search Input
# ============================
selected_movie = st.selectbox(
    "🔎 Search or select a movie:",
    movies['title'].values,
    help="Start typing to search for a movie"
)

# ============================
# Number of Recommendations
# ============================
options = ["5", "10", "15", "20"]
selection = st.segmented_control(
    "Number of Recommendations:",
    options=options,
    default=options[0],
)
top_n = int(selection)

# ============================
# Recommend Button
# ============================
if st.button("🎯 Recommend", use_container_width=True):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie, top_n)

    st.write("### 🔥 Top Recommendations for:", selected_movie)

    # Display movie cards
    for i in range(0, top_n, 5):
        cols = st.columns(5)
        for j, col in enumerate(cols):
            if i + j < top_n:
                with col:
                    st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
                    st.image(posters[i + j], width=220)
                    st.write(f"**{names[i + j]}**")
                    st.markdown("</div>", unsafe_allow_html=True)


