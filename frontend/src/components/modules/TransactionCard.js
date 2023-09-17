import React from 'react';
import { Link } from "react-router-dom";

import "./NavBar.css";

const TransactionCard = (props) => {
  return (
    <div style={{
        display: 'flex',
        justifyContent: 'left',
        alignItems: 'center',
        width: '100%',
        backgroundColor: "#000",
        borderBottom: "1px solid #3E065F",
        borderTop: "1px solid #3E065F"
      }} class="card p-1">

    <div class="card-body">
        <h5 class="card-title">Sep 17, 2023 3:08 AM</h5>
        <p class="card-text">Person A just bought 2 shares of Person B's Crescendo NFTs.</p>
    </div>

    </div>
  )
}

export default TransactionCard