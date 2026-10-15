import streamlit as st
import pandas as pd
import pickle
import os

# ==========================================
# STEP 1: PAGE CONFIGURATION & NETFLIX THEME
# ==========================================
st.set_page_config(
    page_title="CineMatch AI | Advanced Movie Hub",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
    <style>
    .main-title { font-size: 42px; font-weight: 800; color: #E50914; text-align: center; margin-bottom: 10px; }
    .sub-title { font-size: 18px; text-align: center; color: #A0A0A0; margin-bottom: 30px; }
    .movie-card { background-color: #1E1E1E; padding: 20px; border-radius: 10px; border-left: 5px solid #E50914; margin-bottom: 15px; box-shadow: 2px 2px 10px rgba(0,0,0,0.3); }
    .card-title { font-size: 20px; font-weight: 700; color: #FFFFFF; }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# STEP 2: ROBUST DATAFRAME GENERATION
# ==========================================
artifacts_dir = "artifacts"

# We load the dictionary and structural cosine matrix safely
movies_dict = pickle.load(open(os.path.join(artifacts_dir, "movie_dict.pkl"), "rb"))
similarity = pickle.load(open(os.path.join(artifacts_dir, "similarity.pkl"), "rb"))

# Core dataset reference
df = pd.DataFrame(movies_dict)


def clean_string_to_list(val):
    if isinstance(val, str):
        val = val.replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        return [x.strip() for x in val.split(",") if x.strip()]
    return val if isinstance(val, list) else []


df['actors'] = df['actors'].apply(clean_string_to_list)
df['director'] = df['director'].apply(clean_string_to_list)

# ==========================================
# STEP 3: HEADER & SIDEBAR PROFILE layout
# ==========================================

st.markdown("<div class='main-title'>🎬 CineMatch AI: Multi-Search Recommendation Hub</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Discover your next favorite movie using Advanced Machine Learning Vectors Alignment</div>", unsafe_allow_html=True)

st.sidebar.header("⚙️ Engine Configuration")
st.sidebar.info("This system analyzes 4,803 movies across 5,000 unique token dimensions using **Cosine Similarity Calculus**.")
st.sidebar.markdown("---")
st.sidebar.write("📌 **Developer Profile:** SHIVAM SHUKLA")

# ==========================================
# STEP 4: INTERACTIVE TABS MULTI-SEARCH
# ==========================================
tab_movie, tab_actor, tab_director = st.tabs(
    ["🎬 Search by Movie Name", "👤 Search by Star Cast", "🎥 Search by Director"])

# --- TAB 1: MOVIE SEARCH ---
with tab_movie:
    st.subheader("Get Recommendations similar to a Movie")
    selected_movie = st.selectbox("Select a movie you love:", df['title'].values, key="movie_sel")

    if st.button("Generate Movie Matches", key="btn_mov"):
        # Fetching raw integer index position
        idx_arr = df[df['title'] == selected_movie].index
        if len(idx_arr) > 0:
            movie_idx = idx_arr[0]
            distances = similarity[movie_idx]
            sorted_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            st.success(f"Top 5 movies similar to **{selected_movie}**:")
            for rank, item in enumerate(sorted_movies, 1):
                title = df.iloc[item[0]]['title']
                st.markdown(f"<div class='movie-card'><span class='card-title'>{rank}. {title}</span></div>",
                            unsafe_allow_html=True)

# --- TAB 2: ACTOR SEARCH ---
with tab_actor:
    st.subheader("Discover Movies featuring your Favorite Actor")
    all_actors = sorted(list(set([actor for sublist in df['actors'] for actor in sublist])))
    selected_actor = st.selectbox("Select an Actor:", all_actors, key="actor_sel")

    if st.button("Find Actor's Top Movies", key="btn_act"):
        results = []
        for idx, row in df.iterrows():
            if selected_actor in row['actors']:
                results.append(row['title'])

        if results:
            st.success(f"Top movies featuring **{selected_actor}**:")
            for rank, title in enumerate(results[:5], 1):
                st.markdown(f"<div class='movie-card'><span class='card-title'>{rank}. {title}</span></div>",
                            unsafe_allow_html=True)
        else:
            st.warning("No entries found.")

# --- TAB 3: DIRECTOR SEARCH ---
with tab_director:
    st.subheader("Explore the Filmography of a Director")
    all_dirs = sorted(list(set([director for sublist in df['director'] for director in sublist])))
    selected_dir = st.selectbox("Select a Director:", all_dirs, key="dir_sel")

    if st.button("Find Director's Masterpieces", key="btn_dir"):
        results = []
        for idx, row in df.iterrows():
            if selected_dir in row['director']:
                results.append(row['title'])

        if results:
            st.success(f"Masterpieces directed by **{selected_dir}**:")
            for rank, title in enumerate(results[:5], 1):
                st.markdown(f"<div class='movie-card'><span class='card-title'>{rank}. {title}</span></div>",
                            unsafe_allow_html=True)
        else:
            st.warning("No entries found.")
