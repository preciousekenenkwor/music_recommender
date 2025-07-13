import React from 'react';
import { Routes, Route } from 'react-router-dom';
import ArtistGrid from './ArtistGrid';
import ArtistDetail from './ArtistDetail';

const App = () => (
  <Routes>
    <Route path="/" element={<ArtistGrid />} />
    <Route path="/artist/:name" element={<ArtistDetail />} />
  </Routes>
);

export default App;
