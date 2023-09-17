import React from 'react';
import styles from "./solana.css";

import { WalletMultiButton } from "@solana/wallet-adapter-react-ui";
import useIsMounted from '../utils/useIsMounted';

const Solana = () => {
    const mounted = useIsMounted();

    return (
        <div className={styles.container}>
            <div className={styles.navbar}>{mounted && <WalletMultiButton />}</div>

            <div className={styles.main}>
                <h1 className={styles.title}>
                Your First Solana Program with{" "}
                <a href="https://alchemy.com/solana/?a=d0c917f7ef">Alchemy</a>!
                </h1>
            </div>
        </div>
    );
};

// const Home = () => {
//     return (
//       <div
//         style={{
//           display: 'flex',
//           justifyContent: 'top',
//           alignItems: 'top',
//         }}
//       >
//         <NavBar/>
//         <Feed/>
//         <UserInfo/>
//       </div>
//     );
//   };
    
  export default Solana;