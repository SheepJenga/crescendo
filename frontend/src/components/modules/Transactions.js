import React from 'react';
import TransactionCard from './TransactionCard';

const Transactions = (props) => {
  return (
    <div style={{
        display: 'flex',
        justifyContent: 'top',
        alignItems: 'top',
        height: '69vh',
        width: '25%',
        fontFamily: "GameOver",
        fill: "#000"
      }} class="mt-2">
        <div class="card m-3 p-3 w-100 rounded">
        <h1>
            user info
        </h1>
        <TransactionCard/>
        <TransactionCard/>
        <TransactionCard/>
        <TransactionCard/>
        <TransactionCard/>
    </div>
    </div>
  )
}

export default Transactions