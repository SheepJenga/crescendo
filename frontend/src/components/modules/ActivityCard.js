import React from 'react';
import "./ActivityCard.css"

const ActivityCard = (props) => {
  return (
    <div>
<div className="card m-3" style={{borderRadius: '15px'}}>
        <div className="card-body p-4">
          <h3 className="mb-3">Name of NFT</h3>
          <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-2.webp" alt="avatar" className="img-fluid me-1" width={200} />
          <div>
            <audio src="https://learn.shayhowe.com.s3-website-us-east-1.amazonaws.com/assets/misc/courses/html-css/adding-media/jazz.ogg" controls class="m-3"></audio>
          </div>
          <p className="small mb-0"><i className="fas fa-star fa-lg text-warning" /> <span className="mx-2"></span>
            <span className="mx-2"></span>Created on 11 April , 2021
          </p>
          <hr className="my-4" />
          <div className="d-flex justify-content-start align-items-center">
          <div class="comments"></div>
            <p className="mb-0 text-uppercase"><i className="fas fa-cog me-2" /> <span className="text-muted small">Owned by <strong>Username</strong></span></p>
            <p className="mb-0 text-uppercase"><i className="fas fa-link ms-4 me-2" /> <span className="text-muted small">Amount Minted: </span></p>
            <p className="mb-0 text-uppercase"><i className="fas fa-ellipsis-h ms-4 me-2" /> <span className="text-muted small">Supply: </span>
              <span className="ms-3 me-4">|</span></p>
            <a href="#!">
              <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-2.webp" alt="avatar" className="img-fluid rounded-circle me-1" width={35} />
            </a>
          </div>
        </div>
      </div>

      </div>
    
  )
}

export default ActivityCard