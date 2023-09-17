import React from 'react';
import "./ActivityCard.css"

const ActivityCard = (props) => {
  return (
    <div class="tweet-wrap">
  <div class="tweet-header">
    {<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Cotswold_Sheep_%28cropped%29.JPG/440px-Cotswold_Sheep_%28cropped%29.JPG" alt="" class="avator"></img>}
    <div class="tweet-header-info">
      shepard jiang <span>@sheepjenga</span><span> sep 16</span>
    <div>
        <audio src="https://learn.shayhowe.com.s3-website-us-east-1.amazonaws.com/assets/misc/courses/html-css/adding-media/jazz.ogg" controls></audio>
    </div>
    <div>
      <p>BaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaaBaa</p>
    </div>
    </div>
    
  </div>
  <div class="tweet-img-wrap">
    {/* <img src="https://pbs.twimg.com/media/Dgti2h0WkAEUPmT.png" alt="" class="tweet-img"> */}
  </div>
  <div class="tweet-info-counts">
    
    <div class="comments">
      
      <svg class="feather feather-message-circle sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
      <div class="comment-count">69</div>
    </div>
    
    <div class="retweets">
      <svg class="feather feather-repeat sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="17 1 21 5 17 9"></polyline><path d="M3 11V9a4 4 0 0 1 4-4h14"></path><polyline points="7 23 3 19 7 15"></polyline><path d="M21 13v2a4 4 0 0 1-4 4H3"></path></svg>
      <div class="retweet-count">420</div>
    </div>
    
    <div class="likes">
      <svg class="feather feather-heart sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
      <div class="likes-count">
        2.6k
      </div>
    </div>
    </div>
    </div>
  )
}

export default ActivityCard;