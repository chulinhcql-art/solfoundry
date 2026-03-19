from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import os
import json

app = FastAPI(title="SolFoundry Backend - v0.1")

class BountySubmission(BaseModel):
    bounty_id: str
    pr_number: int
    contributor_wallet: str

@app.get("/")
async def root():
    return {"status": "SolFoundry Intelligence Hub Active", "version": "0.1"}

@app.post("/webhook/github")
async def github_webhook(request: Request):
    # Logic xử lý PR từ GitHub để kích hoạt AI Review
    data = await request.json()
    pr_action = data.get("action")
    if pr_action == "opened":
        # Gọi Tay chân Review Bot (ai_review.py)
        os.system("python .github/scripts/ai_review.py")
        return {"msg": "PR Detected. Review Initiated."}
    return {"msg": "Ignored Action"}

@app.get("/wallet/status")
async def get_wallet_status():
    # Đồng bộ với Kế toán Sentinel
    with open("C:/Users/Admin/.openclaw/workspace/memory/wallet_state.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
