# api_backend.py
from fastapi import FastAPI, HTTPException
import pandas as pd
import pickle
import os
import ast

# KYA: FastAPI server instance setup.
app = FastAPI(title="Movie Recommendation Engine API")

# KYA: Saved objects dictionary aur array structure load kar rahe hain.
artifacts_dir = "artifacts"
movies_dict = pickle.load(open(os.path.join(artifacts_dir, "movie_dict.pkl"), "rb"))
similarity = pickle.load(open(os.path.join(artifacts_dir, "similarity.pkl"), "rb"))

df = pd.DataFrame(movies_dict)


# KYA: String lists ko clean iterable lists me convert karne ka filter function.
def clean_string_to_list(val):
    if isinstance(val, str):
        val = val.replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        return [x.strip() for x in val.split(",") if x.strip()]
    return val if isinstance(val, list) else []


df['actors'] = df['actors'].apply(clean_string_to_list)
df['director'] = df['director'].apply(clean_string_to_list)


@app.get("/")
def home():
    return {"message": "CineMatch Enterprise API is fully loaded!"}


# --- 🎬 MOVIE RECOMMENDATION LOGIC ---
# KAISE FIX HUA: (.index[0]) lagakar index object se raw integer row number nikala,
# aur tuple sorting me (x[1]) target kiya taaki similarity score ke basis par accurately sort ho sake.
@app.get("/recommend/movie")
def recommend_by_movie(name: str):
    if name not in df['title'].values:
        raise HTTPException(status_code=404, detail="Movie not found")

    movie_idx = df[df['title'] == name].index[0]
    distances = similarity[movie_idx]
    sorted_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    for i in sorted_movies:
        recommended_titles.append(df.iloc[i[0]]['title'])

    return {"recommendations": recommended_titles}


# --- 👤 ACTOR SEARCH LOGIC ---
@app.get("/recommend/actor")
def recommend_by_actor(name: str):
    movie_titles = []
    for idx, row in df.iterrows():
        if name in row['actors']:
            movie_titles.append(row['title'])
    return {"recommendations": movie_titles[:5]}


# --- 🎥 DIRECTOR SEARCH LOGIC ---
@app.get("/recommend/director")
def recommend_by_director(name: str):
    movie_titles = []
    for idx, row in df.iterrows():
        if name in row['director']:
            movie_titles.append(row['title'])
    return {"recommendations": movie_titles[:5]}
