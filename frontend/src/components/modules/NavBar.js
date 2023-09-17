import React from 'react';
import GoogleLogin, { GoogleLogout } from '@react-oauth/google';
import { Link } from "react-router-dom";

import "./NavBar.css";

const NavBar = (props) => {
  return (
    <div style={{
        display: 'flex',
        justifyContent: 'top',
        alignItems: 'top',
        height: '38vh',
        width: '20%',
        fontFamily: "GameOver",
        position: "sticky",
        top:"8vh",
        zIndex: "500"
      }} class="mt-2">
    
    <div class="card m-3 p-3 w-100 rounded">
        <h1 class="sidebar-title">
            settings
        </h1>
        <a href="/">Home</a>
        <a href="/profile">Profile</a>
        <a href=""></a>
        <a href="#">Link 4</a>
        <a href="#">Link 5</a>
    </div>
    </div>
  )
}

export default NavBar