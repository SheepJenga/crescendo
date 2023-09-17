import React from 'react';
import ActivityCard from './ActivityCard.js'

const Feed = (props) => {
  return (
    <div style={{
        height: '100vh',
        width: '55%',
      }}>
      <ActivityCard/>
      <ActivityCard/>
      <ActivityCard/>
      <ActivityCard/>
    </div>
  )
}

export default Feed