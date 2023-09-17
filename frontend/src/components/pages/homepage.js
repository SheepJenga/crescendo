import React from 'react';
import Feed from '../modules/Feed.js';
import NavBar from '../modules/NavBar.js';
import Transactions from '../modules/Transactions.js';

const Home = () => {
    return (
      <div
        style={{
          display: 'flex',
          justifyContent: 'top',
          alignItems: 'top',
        }}
      >
        <NavBar/>
        <Feed/>
        <Transactions/>
      </div>
    );
  };
    
  export default Home;