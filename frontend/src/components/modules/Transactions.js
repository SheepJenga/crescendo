import React from 'react';
import TransactionCard from './TransactionCard';

const Transactions = (props) => {
  return (
    <div style={{
        display: 'flex',
        justifyContent: 'top',
        alignItems: 'top',
        height: '60vh',
        width: '23%',
        fontFamily: "GameOver",
      }} class="p-2">
        <div class="rounded p-3 w-100">
        <div class="card rounded p-2 w-100">        
        <h1 class="sidebar-title">
            transactions
        </h1></div>
        <TransactionCard/>
        <TransactionCard/>
        <TransactionCard/>
        <TransactionCard/>
    </div>
    </div>
  )
}

export default Transactions