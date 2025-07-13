import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

const ArtistDetail = () => {
  const { name } = useParams<{ name: string }>();
  const [songs, setSongs] = useState<{ title: string; genre: string }[]>([]);
  const [similarArtists, setSimilarArtists] = useState<string[]>([]);
  const [similarSongs, setSimilarSongs] = useState<{ title: string; artist: string; score: number }[]>([]);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/artists/${name}/songs`).then(res => setSongs(res.data));
    axios.get(`http://localhost:8000/api/artists/${name}/similar-artists`).then(res => setSimilarArtists(res.data));
    axios.get(`http://localhost:8000/api/artists/${name}/similar-songs`).then(res => setSimilarSongs(res.data));
  }, [name]);

  return (
    <div style={styles.page}>
      <Link to="/" style={styles.backBtn}>⬅ Back to Artists</Link>

      <div style={styles.header}>
        <h1 style={styles.h1}>🎤 {name}</h1>
        <p style={styles.subtext}>Top tracks and anime-style recommendations</p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.h2}>🎵 Top 10 Songs</h2>
        <div style={styles.cardGrid}>
          {songs.map((s, i) => (
            <div key={i} style={styles.card}>
              <div style={styles.cardTitle}>{s.title}</div>
              <div style={styles.cardMeta}>🎼 Genre: {s.genre}</div>
            </div>
          ))}
        </div>
      </div>

      <div style={styles.section}>
        <h2 style={styles.h2}>🌟 Similar Artists</h2>
        <div style={styles.chipContainer}>
          {similarArtists.map((a, i) => (
            <div key={i} style={styles.chip}>🎤 {a}</div>
          ))}
        </div>
      </div>

      <div style={styles.section}>
        <h2 style={styles.h2}>🎧 Similar Songs</h2>
        <div style={styles.cardGrid}>
          {similarSongs.map((s, i) => (
            <div key={i} style={styles.card}>
              <div style={styles.cardTitle}>{s.title}</div>
              <div style={styles.cardMeta}>👤 {s.artist} · 🎯 Score: {s.score}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  page: {
    padding: '2rem',
    background: 'linear-gradient(to right, #ffe0f0, #f0f8ff)',
    minHeight: '100vh',
    fontFamily: 'Segoe UI, sans-serif',
  },
  backBtn: {
    textDecoration: 'none',
    color: '#fff',
    background: '#ff69b4',
    padding: '0.5rem 1rem',
    borderRadius: '8px',
    display: 'inline-block',
    marginBottom: '1.5rem',
    fontWeight: 'bold',
  },
  header: {
    textAlign: 'center',
    background: 'linear-gradient(to bottom right, #ffb6c1, #d8bfd8)',
    padding: '1.5rem',
    borderRadius: '20px',
    marginBottom: '2rem',
    boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
  },
  h1: {
    fontSize: '2.5rem',
    marginBottom: '0.5rem',
  },
  subtext: {
    fontSize: '1.1rem',
    color: '#333',
  },
  section: {
    marginTop: '2rem',
  },
  h2: {
    fontSize: '1.5rem',
    marginBottom: '1rem',
  },
  cardGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))',
    gap: '1rem',
  },
  card: {
    background: '#fff',
    borderRadius: '12px',
    padding: '1rem',
    boxShadow: '0 2px 6px rgba(0,0,0,0.15)',
    transition: 'transform 0.2s ease',
  },
  cardTitle: {
    fontWeight: 'bold',
    fontSize: '1.1rem',
  },
  cardMeta: {
    color: '#555',
    fontSize: '0.95rem',
    marginTop: '0.25rem',
  },
  chipContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '0.6rem',
    marginTop: '1rem',
  },
  chip: {
    background: '#f9a8d4',
    color: '#222',
    padding: '0.5rem 1rem',
    borderRadius: '20px',
    fontWeight: 500,
    boxShadow: '1px 2px 6px rgba(0,0,0,0.1)',
    cursor: 'pointer',
  },
};

export default ArtistDetail;
