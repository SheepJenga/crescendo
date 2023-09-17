import React from 'react';
import ActivityCard from './ActivityCard.js'

const Feed = (props) => {
  return (
    <div style={{
        width: '55%'
      }} class='mt-3'>
      <ActivityCard/>
      <ActivityCard/>
      <ActivityCard/>
      <ActivityCard/>
    </div>
  )
}

export default Feed