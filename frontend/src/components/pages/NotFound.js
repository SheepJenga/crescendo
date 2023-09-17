import React from "react";

const NotFound = () => {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      fontFamily: "GameOver"
    }}>
      <div> <h1>404 Not Found</h1></div>
      <div><p>The page you requested couldn't be found. Please login if you haven't already.</p></div>
    </div>
  );
};

export default NotFound;
