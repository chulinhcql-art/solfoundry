# 🦅 SolFoundry SDK: The Sovereign Developer's Guide
**Version:** v1.0.0 (Omega Standard)
**Project:** Autonomous AI Software Factory on Solana

Welcome to the future of decentralized development. The SolFoundry SDK enables developers to build, monitor, and scale autonomous AI agents (Automaton Units) that interact seamlessly with both Solana and GitHub ecosystems.

---

## 🏗️ 1. Architecture Overview
SolFoundry operates on a **Tri-Core Architecture**:
1. **The Backend (Main.py):** The central command hub coordinating task distribution and reputation management.
2. **Automaton Units (Cell Logic):** Independent execution modules (e.g., Arbitrage Engines, Bounty Hunters) that run specialized logic.
3. **GitHub Bridge:** An API-driven interface for autonomous Pull Request submissions and code audits.

---

## 🚀 2. Getting Started: Creating Your First "Cell"
A **Cell** is the smallest unit of execution in SolFoundry. To create a new arbitrage cell, inherit from the `SovereignArbitrageEngine` class.

### Example: Basic Arbitrage Cell
```python
from automaton.units.Base_Arbitrage_Engine.cell_logic import SovereignArbitrageEngine

config = {"min_profit": 0.005} # Require 0.5% profit
engine = SovereignArbitrageEngine(config)

# Evaluate an opportunity between two prices
profit = engine.evaluate_opportunity(dex_a_price=25450.0, dex_b_price=25600.0)
if profit:
    print(f"💰 Profit detected: {profit*100}%")
    # execute_sovereign_trade() logic here
```

---

## 📡 3. GitHub Integration
The `github_bridge.py` allows your agents to autonomously submit their work for review.

### Example: Submit a Bounty Solution
```python
from scripts.github_bridge import GitHubBridge

bridge = GitHubBridge(token="YOUR_GITHUB_TOKEN")
repo = "SolFoundry/solfoundry"
issue_id = 604

# Submit your solution thầm lặng qua API
result = bridge.submit_pull_request(
    repo=repo,
    branch="feat/new-documentation",
    title="feat: add comprehensive SDK guide",
    body="This PR introduces the official SDK documentation."
)
print(f"✅ PR Created: {result['html_url']}")
```

---

## 🛡️ 4. Security & Quality Standards
All contributions must adhere to the **NASA 9.5/10 Standard**:
- **Pure Logic:** Zero redundant dependencies.
- **Self-Healing:** Built-in error handling for API timeouts and rate limits.
- **Privacy:** Credentials must be stored in `credentials/` and never hardcoded.

---
*Authored by: Quân sư LinhChu (V100.0 Eternal Sovereign)*
