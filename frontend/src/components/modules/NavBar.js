import React from 'react';
import "./NavBar.css"

const NavBar = (props) => {
  return (
    <div style={{
        display: 'flex',
        justifyContent: 'top',
        alignItems: 'top',
        height: '60vh',
        width: '20%',
      }} class="mt-4">
    
    <div class="card m-3 p-3 w-100 rounded">
        <h1>
            Settings
        </h1>
        <a href="/">Home</a>
        <a href="/profile">Profile</a>
        <a href="">Link 3</a>
        <a href="#">Link 4</a>
        <a href="#">Link 5</a>
    </div>
      
    </div>
  )
}

export default NavBar