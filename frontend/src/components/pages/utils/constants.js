import idl from "../api/idl/solana_hello_world.json";
import { Connection, PublicKey, clusterApiUrl } from "@solana/web3.js";

/* Constants for RPC Connection the Solana Blockchain */
export const commitmentLevel = "processed";
export const endpoint =
  process.env.NEXT_PUBLIC_ALCHEMY_RPC_URL || clusterApiUrl("devnet");
export const connection = new Connection(endpoint, commitmentLevel);

/* Constants for the Deployed "Hello World" Program */
console.log('IDL ', idl)
console.log('META DATA ', idl.metadata)
console.log('ADDRESS ', idl.metadata.address)
export const helloWorldprogramId = new PublicKey(idl.metadata.address);
export const helloWorldprogramInterface = JSON.parse(JSON.stringify(idl));