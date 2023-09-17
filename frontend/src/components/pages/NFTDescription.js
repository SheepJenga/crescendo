import React from "react";
import "./NFTDescription.css";

const NFTDescription = () => {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
    }}>
      <div className="product">
        <div className="image-box">
          <div className="images" id="image-1" />
        </div>
        <div className="text-box">
          <h2 className="item">NFT Name</h2>
          <h3 className="price">$1.90 per share</h3>
          <p className="description">A bag of delicious oranges!</p>
          <label htmlFor="item-1-quantity">Quantity of Shares Remaining:</label>
          <input type="text" name="item-1-quantity" id="item-1-quantity" defaultValue={1} />   (Max: 10)
          <button type="button" name="item-1-button" id="item-1-button">Buy</button>
        </div>
      </div>
    </div>
  
  );
};

export default NFTDescription;
