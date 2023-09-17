import React, { useState, useEffect } from 'react';
import './App.css';
import Header from './/components/header.js';
import Home from './components/pages/homepage.js';
import Solana from './components/pages/solana.js';
import Profile from './components/pages/Profile.js';
import NotFound from './components/pages/NotFound.js';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { PhantomWalletAdapter } from "@solana/wallet-adapter-phantom";
import {
  ConnectionProvider,
  WalletProvider,
} from "@solana/wallet-adapter-react";
import { WalletModalProvider } from "@solana/wallet-adapter-react-ui";
import { endpoint } from "./components/utils/constants";
import "@solana/wallet-adapter-react-ui/styles.css";

function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("http://localhost:8080/").then(
      res => res.json()
    ).then(
      data => setData(data)
    )
  }, [])

  const phantomWallet = new PhantomWalletAdapter();

  return (
    // <div>
    // <BrowserRouter>
    //   <div><Header /></div>
    //   <Routes>
    //     <Route path="/" element={<div class='App-body'><Solana /></div>}>
    //       <Route index element={<Profile/>} />
    //       <Route path="profile" element={<Profile/>} />
    //       <Route path="*" element={<NotFound />} />
    //     </Route>
    //   </Routes>
    // </BrowserRouter>
    // </div>

    <ConnectionProvider endpoint={endpoint}>
      <WalletProvider wallets={[phantomWallet]}>
        <WalletModalProvider>
          {/* <Component {...pageProps} /> */}
          <div>
          <BrowserRouter>
            <div><Header /></div>
            <Routes>
              <Route path="/" element={<div class='App-body'><Home /></div>}>
                <Route index element={<Profile/>} />
                <Route path="profile" element={<Profile/>} />
                <Route path="*" element={<NotFound />} />
              </Route>
            </Routes>
          </BrowserRouter>
          </div>
        </WalletModalProvider>
      </WalletProvider>
    </ConnectionProvider>
    
  );
}

export default App;