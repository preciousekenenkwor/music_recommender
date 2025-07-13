from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import SpotifyTrack
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_artists(skip: int = 0, limit: int = 16, db: Session = Depends(get_db)):
    # 🎨 Get unique artist names, paginated
    artists = (
        db.query(SpotifyTrack.artist_name)
        .distinct()
        .offset(skip)
        .limit(limit)
        .all()
    )
    return [a[0] for a in artists]


@router.get("/{artist_name}/songs")
def get_top_songs(artist_name: str, db: Session = Depends(get_db)):
    # 🎵 Get top 10 most popular songs for this artist
    songs = (
        db.query(SpotifyTrack)
        .filter(SpotifyTrack.artist_name == artist_name)
        .order_by(SpotifyTrack.popularity.desc())
        .limit(10)
        .all()
    )
    return [{"title": s.track_name, "genre": s.genre, "popularity": s.popularity} for s in songs]

@router.get("/{artist_name}/similar-artists")
def similar_artists(artist_name: str, db: Session = Depends(get_db)):
    # 🤝 Recommend similar artists based on sound profile (cosine similarity)
    tracks = db.query(SpotifyTrack).all()
    df = pd.DataFrame([t.__dict__ for t in tracks])
    df = df.drop(columns=["_sa_instance_state", "id", "track_id", "track_name", "genre", "key", "mode", "time_signature"])

    artist_vectors = df.groupby("artist_name").mean(numeric_only=True)
    if artist_name not in artist_vectors.index:
        return []

    sim_scores = cosine_similarity([artist_vectors.loc[artist_name]], artist_vectors)[0]
    artist_vectors["similarity"] = sim_scores
    top_similar = artist_vectors.sort_values("similarity", ascending=False).head(6).iloc[1:]
    return top_similar.index.tolist()

@router.get("/{artist_name}/similar-songs")
def similar_songs(artist_name: str, db: Session = Depends(get_db)):
    # 🎧 Recommend songs similar to the artist’s top song
    top_track = (
        db.query(SpotifyTrack)
        .filter(SpotifyTrack.artist_name == artist_name)
        .order_by(SpotifyTrack.popularity.desc())
        .first()
    )
    if not top_track:
        return []

    all_tracks = db.query(SpotifyTrack).all()
    df = pd.DataFrame([t.__dict__ for t in all_tracks])
    df = df.drop(columns=["_sa_instance_state", "id", "track_id", "genre", "key", "mode", "time_signature"])
    features = df.select_dtypes(include=["float64", "int64"]).fillna(0)

    similarity = cosine_similarity(
        [features[df["track_name"] == top_track.track_name].values[0]],
        features
    )[0]

    df["similarity"] = similarity
    top_similar = df.sort_values("similarity", ascending=False).head(10)
    return [{"title": r["track_name"], "artist": r["artist_name"], "score": round(r["similarity"], 2)}
            for _, r in top_similar.iterrows() if r["artist_name"] != artist_name]
