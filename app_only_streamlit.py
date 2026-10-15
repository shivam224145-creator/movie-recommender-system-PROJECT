# app_only_streamlit.py
import streamlit as str_app
import pandas as pd
import pickle
import os

str_app.set_page_config(page_title="AI Movie Recommender", page_icon="🎬", layout="centered")

artifacts_dir = "artifacts"
movies_dict = pickle.load(open(os.path.join(artifacts_dir, "movie_dict.pkl"), "rb"))
similarity = pickle.load(open(os.path.join(artifacts_dir, "similarity.pkl"), "rb"))

df = pd.DataFrame(movies_dict)

# --- WEB UI FRONTEND ---
str_app.title("🎬 AI-Powered Movie Recommendation System")
str_app.write("Select a movie you love, and the ML engine will suggest similar ones based on directors and lead cast!")


movie_list = df['title'].values
selected_movie = str_app.selectbox("Type or select a movie name:", movie_list)


# --- CORE RECOMMENDATION FUNCTION ---

def get_recommendations(movie_name):

    movie_idx = df[df['title'] == movie_name].index[0]

    distances = similarity[movie_idx]
    sorted_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    for i in sorted_movies:
        recommended_titles.append(df.iloc[i[0]]['title'])
    return recommended_titles


# --- UI BUTTON TRIGGER ---
if str_app.button("Recommend Similar Movies"):
    with str_app.spinner('AI Engine is calculating vectors proximity...'):
        recommendations = get_recommendations(selected_movie)

        str_app.success("Here are the top 5 movies you might also like:")

        for index, movie in enumerate(recommendations, 1):
            str_app.markdown(f"**{index}.** {movie}")
