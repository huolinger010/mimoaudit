# 🛡 SmartAudit — AI Smart Contract Auditor

**Powered by Xiaomi MiMo V2.5**

Free, instant smart contract security auditor that detects vulnerabilities, optimizes gas usage, and provides actionable security recommendations. **No API key required.**

![SmartAudit](https://img.shields.io/badge/Powered%20by-Xiaomi%20MiMo-6c5ce7?style=for-the-badge)
![Free](https://img.shields.io/badge/Price-100%25%20Free-brightgreen?style=for-the-badge)
![Solidity](https://img.shields.io/badge/Solidity-0.8.x-363636?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🚀 Features

- **100% Free** — No API key, no registration, no cost
- **40+ Detection Rules** — Comprehensive vulnerability scanning
- **Multi-Chain Support** — Ethereum, Base, Arbitrum, Optimism, Polygon, BSC, Avalanche, zkSync
- **Auto Source Fetch** — Enter a contract address, get source code from Blockscout automatically
- **Instant Analysis** — Results in seconds, no waiting
- **Security Audit**:
  - Reentrancy vulnerabilities
  - Access control issues
  - Integer overflow/underflow
  - Unchecked external calls
  - Front-running vulnerabilities
  - Centralization risks
  - Missing events
  - Timestamp dependence
  - Denial of service vectors
  - Delegatecall risks
  - Selfdestruct usage
  - Insecure randomness
  - And 25+ more rules
- **Risk Scoring** — 0-100 risk score with severity breakdown
- **Gas Optimization** — Actionable suggestions to reduce gas costs
- **Sample Contracts** — Try with built-in vulnerable contract examples
- **Report Export** — Download full audit report as text file
- **Zero Backend** — Runs entirely in browser

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
3. **Analyze** — Pattern-based engine checks 40+ security rules
4. **Report** — Get risk score, detailed findings, and gas optimization suggestions

## 🎯 Why SmartAudit?

| Traditional Audit | SmartAudit |
|---|---|
| $5K-$50K+ per audit | **Free** |
| Weeks of waiting | **Instant** |
| Limited availability | **24/7 available** |
| Human error prone | **Consistent analysis** |
| Requires trust | **Transparent rules** |

## 🔍 Detection Rules

### Critical
- Reentrancy vulnerabilities
- Delegatecall usage
- Selfdestruct usage
- Insecure randomness
- Division by zero
- Missing SafeMath (Solidity <0.8)

### High
- Missing access control
- Unchecked external calls
- tx.origin authorization
- Proxy contract patterns

### Medium
- ERC-20 approve front-running
- Front-running potential
- Denial of service vectors
- Unchecked arithmetic
- Missing reentrancy guard

### Low/Info
- Block timestamp dependence
- Missing events
- Centralization risks
- Gas optimization opportunities

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
