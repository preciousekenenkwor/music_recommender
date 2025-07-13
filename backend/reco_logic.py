import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr
from sqlalchemy.orm import Session
from models import SpotifyTrack

# Get all track data into a DataFrame
def load_tracks(session: Session):
    tracks = session.query(SpotifyTrack).all()
    return pd.DataFrame([{
        "track_id": t.track_id,
        "title": t.track_name,
        "artist": t.artist_name,
        "genre": t.genre,
        "popularity": t.popularity,
        "acousticness": t.acousticness,
        "danceability": t.danceability,
        "duration_ms": t.duration_ms,
        "energy": t.energy,
        "instrumentalness": t.instrumentalness,
        "liveness": t.liveness,
        "loudness": t.loudness,
        "speechiness": t.speechiness,
        "tempo": t.tempo,
        "valence": t.valence
    } for t in tracks])

# Simple clustering recommendation
def cluster_based_recommendation(df, n_clusters=5):
    features = df[["acousticness", "danceability", "energy", "valence", "tempo"]]
    scaled = StandardScaler().fit_transform(features)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["cluster"] = kmeans.fit_predict(scaled)
    return df

# User-based CF (mocked user prefs)
def user_cf(df, user_history):
    user_vector = df[df['track_id'].isin(user_history)].drop(columns=["track_id", "title", "artist", "genre", "cluster"])
    mean_vector = user_vector.mean().values.reshape(1, -1)
    track_vectors = df.drop(columns=["track_id", "title", "artist", "genre", "cluster"])
    similarities = cosine_similarity(mean_vector, track_vectors)[0]
    df["similarity"] = similarities
    reco = df[~df["track_id"].isin(user_history)].sort_values("similarity", ascending=False)
    return reco[["title", "artist", "genre", "similarity"]].head(10)

# Pearson similarity for diversity
def pearson_similarity(track_a, track_b):
    common = track_a.index.intersection(track_b.index)
    if len(common) < 2:
        return 0
    return pearsonr(track_a[common], track_b[common])[0]
