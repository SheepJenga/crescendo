import React from 'react';
import Feed from '../modules/Feed.js';
import NavBar from '../modules/NavBar.js';
import UserInfo from '../modules/UserInfo.js';

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
        <UserInfo/>
      </div>
    );
  };
    
  export default Home;