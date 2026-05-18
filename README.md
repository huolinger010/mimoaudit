# 🛡 SmartAudit — AI Smart Contract Auditor

**Powered by Xiaomi MiMo V2.5**

AI-powered smart contract security auditor that detects vulnerabilities, optimizes gas usage, and provides actionable security recommendations — all through natural language analysis powered by Xiaomi MiMo.

![SmartAudit](https://img.shields.io/badge/Powered%20by-Xiaomi%20MiMo-6c5ce7?style=for-the-badge)
![Solidity](https://img.shields.io/badge/Solidity-0.8.x-363636?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🚀 Features

- **AI-Powered Analysis** — Uses Xiaomi MiMo V2.5 to deeply analyze Solidity smart contracts
- **Multi-Chain Support** — Ethereum, Base, Arbitrum, Optimism, Polygon, BSC, Avalanche, zkSync
- **Auto Source Fetch** — Enter a contract address and get source code from Blockscout automatically
- **Comprehensive Security Audit**:
  - Reentrancy vulnerabilities
  - Integer overflow/underflow
  - Access control issues
  - Unchecked external calls
  - Front-running vulnerabilities
  - Centralization risks
  - Missing events
  - Timestamp dependence
  - Denial of service vectors
- **Risk Scoring** — 0-100 risk score with severity breakdown (Critical/High/Medium/Low/Info)
- **Gas Optimization** — Actionable suggestions to reduce gas costs
- **Report Export** — Download full audit report as text file
- **Zero Backend** — Runs entirely in browser, no server needed

## 🏗 Architecture

```
┌─────────────────────────────────────────────┐
│                  Browser                     │
│  ┌─────────┐  ┌──────────┐  ┌────────────┐ │
│  │   UI    │  │ Blockscout│  │  MiMo API  │ │
│  │ (HTML)  │──│   API     │  │ (V2.5 Pro) │ │
│  └─────────┘  └──────────┘  └────────────┘ │
│       │                           │         │
│       └───────────┬───────────────┘         │
│                   ▼                         │
│          Security Report                    │
└─────────────────────────────────────────────┘
```

## 📖 How It Works

1. **Input** — Enter a verified contract address OR paste Solidity source code
2. **Fetch** — Blockscout API retrieves verified contract source code (if address provided)
3. **Analyze** — Xiaomi MiMo V2.5 performs deep security analysis
4. **Report** — Get risk score, detailed findings, and gas optimization suggestions

## 🔧 Usage

### Online (GitHub Pages)
Visit: `https://gyoomei.github.io/smartaudit/`

### Local
Simply open `index.html` in your browser. No build step needed.

### API Key
You need a Xiaomi MiMo API key:
1. Visit [Xiaomi MiMo Platform](https://platform.xiaomimimo.com)
2. Register and get your API key
3. Enter it when prompted in the app

## 🎯 Why SmartAudit?

| Traditional Audit | SmartAudit |
|---|---|
| $5K-$50K+ per audit | Free (API costs only) |
| Weeks of waiting | Minutes |
| Limited availability | 24/7 available |
| Human error prone | Consistent AI analysis |

## 🔍 Example Findings

SmartAudit detects common vulnerabilities:

- **Reentrancy** — Unprotected external calls that can be exploited
- **Access Control** — Missing or incorrect permission checks
- **Integer Overflow** — Arithmetic operations without SafeMath
- **Front-Running** — Transactions that can be sandwiched
- **Gas Waste** — Redundant storage reads, unchecked loops

## 🛠 Built With

- **Xiaomi MiMo V2.5** — AI reasoning and analysis
- **Blockscout API** — Multi-chain contract source code retrieval
- **Vanilla HTML/CSS/JS** — Zero dependencies, instant load

## 📄 License

MIT License — see [LICENSE](LICENSE)

## 🙏 Acknowledgments

- [Xiaomi MiMo](https://mimo.xiaomi.com/) — AI model powering the analysis
- [Blockscout](https://www.blockscout.com/) — Open-source blockchain explorer
- [MiMo 100T Creator Program](https://100t.xiaomimimo.com/) — Token incentive program

---

**Built for the Xiaomi MiMo 100T Token Creator Incentive Program**
