# app_with_fastapi.py
import streamlit as st
import pandas as pd
import pickle
import requests
import os

# KYA: Netflix style layout web interface template set kar rahe hain.
st.set_page_config(page_title="CineMatch AI Pro Portal", page_icon="🎬", layout="wide")

# Custom Netflix UI styling configuration
st.markdown("""
    <style>
    .main-title { font-size: 42px; font-weight: 800; color: #E50914; text-align: center; margin-bottom: 10px; }
    .sub-title { font-size: 18px; text-align: center; color: #A0A0A0; margin-bottom: 30px; }
    .movie-card { background-color: #1E1E1E; padding: 20px; border-radius: 10px; border-left: 5px solid #E50914; margin-bottom: 15px; box-shadow: 2px 2px 10px rgba(0,0,0,0.3); }
    .card-title { font-size: 20px; font-weight: 700; color: #FFFFFF; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🎬 CineMatch AI: Microservice Architecture Hub</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>Highly Optimized Recommendations Powered by FastAPI & Streamlit Frontend Engine</div>",
    unsafe_allow_html=True)

# Sidebar setup
st.sidebar.header("⚙️ Server Node Status")
st.sidebar.success("Client Connected to Local Host Gateway.")
st.sidebar.markdown("---")
st.sidebar.write("📌 **Developer Profile:** SHIVAM SHUKLA")

# Dropdown options parsing arrays initialization
artifacts_dir = "artifacts"
movies_dict = pickle.load(open(os.path.join(artifacts_dir, "movie_dict.pkl"), "rb"))
df = pd.DataFrame(movies_dict)


def clean_string_to_list(val):
    if isinstance(val, str):
        val = val.replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        return [x.strip() for x in val.split(",") if x.strip()]
    return val if isinstance(val, list) else []


df['actors'] = df['actors'].apply(clean_string_to_list)
df['director'] = df['director'].apply(clean_string_to_list)

# KYA: Connection routing endpoint config
BASE_API_URL = "http://localhost:8000"

# Horizontal tabs creation blocks
tab_movie, tab_actor, tab_director = st.tabs(
    ["🎬 Search by Movie Name", "👤 Search by Star Cast", "🎥 Search by Director"])

# --- TAB 1: MOVIE SEARCH ---
with tab_movie:
    st.subheader("Get Recommendations similar to a Movie")
    selected_movie = st.selectbox("Select a movie you love:", df['title'].values, key="movie_sel")

    if st.button("Generate Movie Matches", key="btn_mov"):
        with st.spinner('Fetching vectors from API...'):
            try:
                response = requests.get(f"{BASE_API_URL}/recommend/movie", params={"name": selected_movie})
                if response.status_code == 200:
                    recs = response.json()["recommendations"]
                    if recs:
                        st.success(f"Top 5 movies similar to **{selected_movie}**:")
                        for idx, m in enumerate(recs, 1):
                            st.markdown(f"<div class='movie-card'><span class='card-title'>{idx}. {m}</span></div>",
                                        unsafe_allow_html=True)
                    else:
                        st.warning("No results returned from model mapping.")
                else:
                    st.error("API response code validation failed.")
            except:
                st.error("Backend Server is unresponsive.")

# --- TAB 2: ACTOR SEARCH ---
with tab_actor:
    st.subheader("Discover Movies featuring your Favorite Actor")
    all_actors = sorted(list(set([actor for sublist in df['actors'] for actor in sublist if actor])))
    selected_actor = st.selectbox("Select an Actor:", all_actors, key="actor_sel")

    if st.button("Find Actor's Top Movies", key="btn_act"):
        with st.spinner('Accessing database registry via FastAPI...'):
            try:
                response = requests.get(f"{BASE_API_URL}/recommend/actor", params={"name": selected_actor})
                if response.status_code == 200:
                    recs = response.json()["recommendations"]
                    if recs:
                        st.success(f"Top movies featuring **{selected_actor}**:")
                        for idx, m in enumerate(recs, 1):
                            st.markdown(f"<div class='movie-card'><span class='card-title'>{idx}. {m}</span></div>",
                                        unsafe_allow_html=True)
                    else:
                        st.warning("No movies found.")
            except:
                st.error("Backend Connection Error.")

# --- TAB 3: DIRECTOR SEARCH ---
with tab_director:
    st.subheader("Explore the Filmography of a Director")
    all_dirs = sorted(list(set([director for sublist in df['director'] for director in sublist if director])))
    selected_dir = st.selectbox("Select a Director:", all_dirs, key="dir_sel")

    if st.button("Find Director's Masterpieces", key="btn_dir"):
        with st.spinner('Querying deployment network clusters...'):
            try:
                response = requests.get(f"{BASE_API_URL}/recommend/director", params={"name": selected_dir})
                if response.status_code == 200:
                    recs = response.json()["recommendations"]
                    if recs:
                        st.success(f"Masterpieces directed by **{selected_dir}**:")
                        for idx, m in enumerate(recs, 1):
                            st.markdown(f"<div class='movie-card'><span class='card-title'>{idx}. {m}</span></div>",
                                        unsafe_allow_html=True)
                    else:
                        st.warning("No movies found.")
            except:
                st.error("Backend Connection Error.")
