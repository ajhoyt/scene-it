import streamlit as st
import requests

# TMDb API Key
API_KEY = "9a74e7ca253e501d29b12d0797c12c69"
BASE_URL = "https://api.themoviedb.org/3"

def search_movies(query):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}"
    response = requests.get(url)
    return response.json().get('results', [])

# Streamlit Interface
st.title("SceneIt: Discover Your Next Movie!")
movie_query = st.text_input("Search for a movie:")

if movie_query:
    movies = search_movies(movie_query)
    for movie in movies:
        st.write(f"**{movie['title']}** ({movie['release_date'][:4] if movie.get('release_date') else 'N/A'})")
        st.image(f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get('poster_path') else "", width=150)