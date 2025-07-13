from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from reco_logic import load_tracks, cluster_based_recommendation, user_cf

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}")
def recommend(user_id: str, db: Session = Depends(get_db)):
    # Dummy user listening history (track_ids)
    user_history = ["0BRjO6ga9RKCKjfDqeFgWV"]
    df = load_tracks(db)
    df = cluster_based_recommendation(df)
    recommendations = user_cf(df, user_history)
    return recommendations.to_dict(orient="records")
