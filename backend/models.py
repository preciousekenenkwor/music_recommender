from sqlalchemy import Column, Integer, String, Float
from database import Base

class SpotifyTrack(Base):
    __tablename__ = "spotify_tracks"

    id = Column(Integer, primary_key=True, index=True)
    genre = Column(String)
    artist_name = Column(String)
    track_name = Column(String)
    track_id = Column(String, unique=True, index=True)
    popularity = Column(Integer)
    acousticness = Column(Float)
    danceability = Column(Float)
    duration_ms = Column(Integer)
    energy = Column(Float)
    instrumentalness = Column(Float)
    key = Column(String)
    liveness = Column(Float)
    loudness = Column(Float)
    mode = Column(String)
    speechiness = Column(Float)
    tempo = Column(Float)
    time_signature = Column(String)
    valence = Column(Float)
