use anchor_lang::prelude::*;

declare_id!("B1djBFNqSDoGUauSAfntHswvYMEtQiYRgt3RqbTtQw59");

#[program]
pub mod solana_hello_world {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {}
