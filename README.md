# 🛡 MimoAudit — AI Smart Contract Auditor

**Powered by Xiaomi MiMo V2.5**

Free, instant smart contract security auditor that detects vulnerabilities, optimizes gas usage, and provides actionable security recommendations. **No API key required.**

![MimoAudit](https://img.shields.io/badge/Powered%20by-Xiaomi%20MiMo-6c5ce7?style=for-the-badge)
![Free](https://img.shields.io/badge/Price-100%25%20Free-brightgreen?style=for-the-badge)
![Solidity](https://img.shields.io/badge/Solidity-0.8.x-363636?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> Live: https://gyoomei.github.io/mimoaudit/

## 🚀 Features

- **100% Free** — No API key, no registration, no cost
- **40+ Detection Rules** — Comprehensive vulnerability scanning
- **Multi-Chain Support** — Ethereum, Base, Arbitrum, Optimism, Polygon, BSC, Avalanche, zkSync
- **Auto Source Fetch** — Enter a contract address, get source code from Blockscout automatically
- **Instant Analysis** — Results in seconds, no waiting
- **Severity Filter & Search** — Drill down into specific findings instantly
- **Scan History** — Last 10 scans saved locally, one-click reload
- **Multi-Format Export** — TXT, Markdown, or JSON
- **Shareable Reports** — Copy a permalink that contains your source code (URL fragment, never sent to a server)
- **Contract Overview** — Inspect parsed structure: contracts, functions, state variables, modifiers
- **Risk Scoring** — 0-100 risk score with severity breakdown
- **Gas Optimization** — Actionable suggestions to reduce gas costs
- **Sample Contracts** — Try with built-in vulnerable contract examples
- **Zero Backend** — Runs entirely in browser, no data leaves your machine

## 🔬 What It Detects

### Critical
- Reentrancy vulnerabilities
- Delegatecall usage
- Selfdestruct (especially without auth)
- Insecure randomness (block.timestamp/keccak256)
- tx.origin authorization
- Missing access control on sensitive functions
- Missing SafeMath (Solidity <0.8)

### High
- Unchecked external calls / .send()
- Stale oracle price (Chainlink missing checks)
- Proxy storage collision risks

### Medium
- ERC-20 approve front-running
- Front-running / MEV (no slippage)
- Denial of service (unbounded loops, push payments)
- Unchecked arithmetic blocks
- Missing reentrancy guard

### Low / Info
- Block timestamp dependence
- Missing events on state changes
- Centralization risks
- Could-be-external functions
- Could-be-immutable variables
- Inline assembly usage
- Gas optimization opportunities (cache length, ++i, calldata, struct packing, etc.)

## 🏗 Architecture

```
┌─────────────────────────────────────────────┐
│                  Browser                     │
│  ┌─────────┐  ┌──────────┐  ┌────────────┐ │
│  │   UI    │  │ Blockscout│  │  Pattern   │ │
│  │ (HTML)  │──│   API     │──│  Analyzer  │ │
│  └─────────┘  └──────────┘  └────────────┘ │
│                   │                │         │
│                   └───────┬───────┘         │
│                           ▼                 │
│                  Security Report            │
└─────────────────────────────────────────────┘
```

## 📖 How It Works

1. **Input** — Enter a verified contract address OR paste Solidity source code
2. **Fetch** — Blockscout API retrieves verified contract source code
3. **Parse** — Lightweight Solidity parser extracts contracts, functions, modifiers, state vars
4. **Analyze** — Pattern-based engine checks 40+ security rules
5. **Report** — Get risk score, detailed findings, gas tips, and exportable report

## 🎯 Why MimoAudit?

| Traditional Audit | MimoAudit |
|---|---|
| $5K-$50K+ per audit | **Free** |
| Weeks of waiting | **Instant** |
| Limited availability | **24/7 available** |
| Human error prone | **Consistent analysis** |
| Requires trust | **Transparent, open-source rules** |

## ⌨️ Keyboard Shortcuts

- `Ctrl/Cmd + Enter` — Analyze
- `/` — Focus input
- `Esc` — New scan

## 🛠 Built With

- **Xiaomi MiMo** — AI inspiration for analysis patterns
- **Blockscout API** — Multi-chain contract source code retrieval
- **Vanilla HTML/CSS/JS** — Zero dependencies, instant load

## 📄 License

MIT License — see [LICENSE](LICENSE)

## 🙏 Acknowledgments

- [Xiaomi MiMo](https://mimo.xiaomi.com/) — AI model inspiration
- [Blockscout](https://www.blockscout.com/) — Open-source blockchain explorer
- [MiMo 100T Creator Program](https://100t.xiaomimimo.com/) — Token incentive program

---

**Built for the Xiaomi MiMo 100T Token Creator Incentive Program**
