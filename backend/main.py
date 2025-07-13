from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes.recommendations import router as reco_router
from routes.auth import router as auth_router
from routes.artist import router as artist_router

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth")
app.include_router(reco_router, prefix="/recommendations")
app.include_router(artist_router, prefix="/api/artists")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Music Recommender System API"}
