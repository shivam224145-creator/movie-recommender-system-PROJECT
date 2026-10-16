# Movie-Recommendation-System-streamlit-deployment

---

## "An intelligent movie discovery hub deployed on Streamlit Cloud. It extracts deep structural tags to calculate high-dimensional matrix proximity for personalized recommendations."

---

# 🎬 CineMatch AI: Content-Based Movie Recommender System

An intelligent, end-to-end movie discovery hub powered by Machine Learning and Natural Language Processing (NLP). This production-grade application vectorizes movie metadata and uses vector space mathematical alignments to deliver highly personalized top 5 movie recommendations in real-time.

🌐 **Live Deployment Link:** https://movie-recommendation-system-app-deployment-ovt4kliagsgbzbprqwa.streamlit.app/

---

## 🚀 Key Features
* **Multi-Search Functionality :** Users can seamlessly discover movies across three interactive horizontal tabs:
  * 🎬 **Search by Movie Name:** Recommends 5 visually matching movies based on metadata similarities.
  * 👤 **Search by Star Cast:** Automatically filters the filmography and highlights top movies of a selected actor.
  * 🎥 **Search by Director:** Pulls masterpieces directed by the chosen film director.
* **Netflix-Style Dark Aura UI:** Built a highly attractive, responsive web layout with custom HTML/CSS glowing red-border grid cards.
* **Optimized Storage Matrix:** Engineered data down to the top 1500 most popular movies, compressing the mathematical matrices to under 40MB for lightning-fast server deployment without a millimeter of lag.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Natural Language Processing:** NLTK (Natural Language Toolkit), PorterStemmer
* **Machine Learning Calculus:** Scikit-Learn (CountVectorizer, Pairwise Cosine Similarity)
* **Model Serialization:** Pickle, Object Binary Utilities
* **Frontend Web UI & Framework:** Streamlit (Wide-Layout Wrapper Engine)

---

## 🧠 System Architecture & Workflow

### Phase 1: Data Acquisition & Structural Integrity (Day 1)
* Loaded raw textual TMDB attributes (`movie_id`, `title`, `cast`, `crew`) into operational Pandas dataframes.

### Phase 2: Data Cleaning & JSON Transformation (Day 2)
* Evaluated stringified complex arrays safely using `ast.literal_eval()`.
* Extracted top 5 main lead actors from the cast list and stripped whitespace characters (e.g., `'Sam Worthington'` ➡️ `'SamWorthington'`) to avoid NLP unique token mismatch.
* Parsed crew metrics to dynamically isolate and capture the explicit Film Director.

### Phase 3: Tokenization & High-Dimensional Matrix (Day 3)
* Concatenated individual string blocks into a cohesive `tags` vector segment.
* Applied **PorterStemmer (Stemming)** to standardize contextual variation flags (e.g., *loved, loving, loves* ➡️ *love*).
* Transformed normalized strings using **CountVectorizer (Bag of Words)** to isolate the top 5000 unique categorical token dimensions.

### Phase 4: Cosine Similarity & Model Serialization (Day 4)
* Calculated dot-product proximity scores using **Cosine Similarity Calculus** to build a coordinate distance matrix map.
* Serialized processed models safely to disk files (`movie_dict.pkl`, `similarity.pkl`).

### Phase 5 & 6: Application Layer & Microservice (Day 5 & Day 6)
* Developed and validated localized standard scripts. Explored enterprise microservice frameworks using decoupled **FastAPI** backend routing systems and requests controllers.

### Phase 7: Public Cloud Production (Day 7)
* Integrated source code repositories directly onto **Streamlit Community Cloud Infrastructure** to make the system accessible globally.

---

## 📁 Repository Structure
```text
├── artifacts/             # Pre-calculated serialized model binaries (.pkl files)
├── data/
│   ├── raw/               # Original raw source files
│   └── processed/         # Intermediate parsed tables
├── notebooks/             # Data Research & Engineering Sandbox (Jupyter Files)
├── app.py                 # Core Streamlit Web Application entry point
├── requirements.txt       # Global production environment dependencies
└── README.md              # Software system overview layout
```

---
