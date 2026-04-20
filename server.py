from fastapi import FastAPI
from fzmovies_api import search, get_movie

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/search")
def search_movies(query: str):
    return search(query)

@app.get("/movie")
def movie_details(url: str):
    return get_movie(url)