import React from 'react';

const UserInfo = (props) => {
  return (
    <div style={{
        display: 'flex',
        justifyContent: 'top',
        alignItems: 'top',
        height: '80vh',
        width: '25%',
      }} class="mt-4">
        <div class="card m-3 p-3 w-100 rounded">
        <h1>
            User Information
        </h1>
        <a href="#">Link 1</a>
        <a href="#">Link 2</a>
        <a href="#">Link 3</a>
        <a href="#">Link 4</a>
        <a href="#">Link 5</a>
    </div>
    </div>
  )
}

export default UserInfo