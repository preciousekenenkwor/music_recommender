# 🎵 Anime-Themed Music Recommender System

A vibrant full-stack music recommendation app styled with anime visuals. It uses real Spotify track and artist data stored in PostgreSQL and serves intelligent recommendations through clustering, collaborative filtering, cosine/Pearson similarity, and hybrid logic.

![paul poto](https://github.com/user-attachments/assets/4c8361ad-5544-42e8-a546-70b6c3d1963f)


## ⚙ Backend Setup (No requirements.txt file)

> Make sure you have *Python 3.9+* and *PostgreSQL* installed. The database is already preloaded with Spotify data.

### 🛠 Manual Installation

```bash
# 1. Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# 2. Install backend dependencies
pip install fastapi uvicorn psycopg2 sqlalchemy pandas numpy scikit-learn
