import React, { useState, useEffect } from 'react'
import './App.css';

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
      <p>
        {data.score}
        {console.log(data)}
      </p>
    </div>
  );
}

export default App;
