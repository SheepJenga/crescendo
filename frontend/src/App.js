import React, { useState } from 'react'
import './App.css';

function App() {
  const [data, setData] = useState("")

  useEffect(() => {
    fetch("/").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  return (
    <div>
      <p>
        {data}
      </p>
    </div>
  );
}

export default App;
