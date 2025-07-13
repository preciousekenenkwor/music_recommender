import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './style.css';

const ArtistGrid = () => {
  const [artists, setArtists] = useState<string[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get("http://localhost:8000/api/artists")
      .then(res => setArtists(res.data))
      .catch(err => console.error("Failed to fetch artists", err));
  }, []);

  return (
    <div className="grid">
      <h1 className="title">🎶 Anime Music Recommender</h1>
      <div className="artist-grid">
        {artists.map((artist, idx) => (
          <div key={idx} className="artist-card" onClick={() => navigate(`/artist/${encodeURIComponent(artist)}`)}>
            <div className="artist-image anime-bg" />
            <h3>{artist}</h3>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ArtistGrid;
