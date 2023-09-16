import React, { useState, useEffect } from 'react';
import './App.css';
import Header from './/components/header.js';
import Home from './components/pages/homepage.js';
import Feed from './components/pages/feed.js'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


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
    <Router>
      <Header />
      <Routes>
        <Route path='/' exact component={Home} />
        <Route path='/feed' component={Feed} />
      </Routes>
    </Router>
    <div>
      <p>
        {data.score}
        {console.log(data)}
      </p>
    </div>
    </div>
  );
}

export default App;