import React, { useState, useEffect } from 'react';
import './App.css';
import Header from './/components/header.js';
import Home from './components/pages/homepage.js';
import Profile from './components/pages/Profile.js';
import NotFound from './components/pages/NotFound.js';
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("http://localhost:8080/").then(
      res => res.json()
    ).then(
      data => setData(data)
    )
  }, [])

  return (
    <div>
    <Header />
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>}>
          <Route index element={<Profile/>} />
          <Route path="profile" element={<Profile/>} />
          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>
    </BrowserRouter>
    </div>
    
  );
}

export default App;