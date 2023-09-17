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
      }} class="mt-2">
        <div class="rounded p-3 w-100">
        <div class="card rounded pt-2 w-100">        
        <h1 class="title">
            transactions
        </h1></div>
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