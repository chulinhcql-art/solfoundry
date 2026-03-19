use anchor_lang::prelude::*;

declare_id!("C2TvY8E8B75EF2UP8cTpTp3EDUjTgjWmpaGnT74VBAGS");

#[program]
pub mod solfoundry {
    use super::*;

    pub fn initialize_bounty(ctx: Context<InitializeBounty>, amount: u64, id: String) -> Result<()> {
        let bounty = &mut ctx.accounts.bounty;
        bounty.id = id;
        bounty.amount = amount;
        bounty.status = BountyStatus::Open;
        bounty.creator = ctx.accounts.creator.key();
        msg!("Bounty {} initialized with {} $FNDRY", bounty.id, bounty.amount);
        Ok(())
    }

    pub fn complete_bounty(ctx: Context<CompleteBounty>) -> Result<()> {
        let bounty = &mut ctx.accounts.bounty;
        require!(bounty.status == BountyStatus::Open, ErrorCode::BountyNotOpen);
        
        bounty.status = BountyStatus::Completed;
        bounty.winner = ctx.accounts.winner.key();
        
        msg!("Bounty {} completed. Winner: {}", bounty.id, bounty.winner);
        // Transfer logic will be added in Phase 2 with Escrow PDA
        Ok(())
    }
}

#[derive(Accounts)]
#[instruction(amount: u64, id: String)]
pub struct InitializeBounty<'info> {
    #[account(init, payer = creator, space = 8 + 32 + 8 + 1 + 32 + 32)]
    pub bounty: Account<'info, Bounty>,
    #[account(mut)]
    pub creator: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct CompleteBounty<'info> {
    #[account(mut)]
    pub bounty: Account<'info, Bounty>,
    pub winner: Signer<'info>,
}

#[account]
pub struct Bounty {
    pub id: String,
    pub amount: u64,
    pub status: BountyStatus,
    pub creator: Pubkey,
    pub winner: Pubkey,
}

#[derive(AnchorSerialize, AnchorDeserialize, Clone, PartialEq, Eq)]
pub enum BountyStatus {
    Open,
    Completed,
    Disputed,
}

#[error_code]
pub enum ErrorCode {
    #[msg("The bounty is not open for completion.")]
    BountyNotOpen,
}
