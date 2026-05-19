# 🛡 MimoAudit — AI-Powered Web3 Security Suite

**Powered by Xiaomi MiMo V2.5**

A complete browser-based Web3 security toolkit: smart contract auditor, wallet approval scanner, diff audit, AI assistant, auto-fix templates, and a Famous DeFi Hacks gallery. **No API key. No signup. 100% free.**

![MimoAudit](https://img.shields.io/badge/Powered%20by-Xiaomi%20MiMo-6c5ce7?style=for-the-badge)
![Free](https://img.shields.io/badge/Price-100%25%20Free-brightgreen?style=for-the-badge)
![Solidity](https://img.shields.io/badge/Solidity-0.8.x-363636?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Live:** https://huolinger010.github.io/mimoaudit/

---

## ✨ Six Tools in One

### 🛡 1. Smart Contract Auditor
- **40+ detection rules** across critical → info severity
- **Multi-chain** — Ethereum, Base, Arbitrum, Optimism, Polygon, BSC, Avalanche, zkSync
- **Auto source fetch** from Blockscout — paste an address, get verified source instantly
- **Risk scoring** 0–100 with severity breakdown
- **Gas optimization** suggestions
- **Severity filter + search**, **scan history** (last 10 saved locally)
- **Export** as TXT / Markdown / JSON, **share** via URL fragment (source stays in URL, never on a server)

### 🔓 2. Wallet Approval Scanner
- Paste any wallet address — see every active ERC-20 approval
- **Risk scoring**: `UNLIMITED` → critical, large → high, normal → medium/low
- **Sorted by risk** so the dangerous ones surface first
- **One-click revoke.cash link** with the right chain pre-selected
- Powered by Blockscout's `getLogs` API — no API key, no third-party tracking

### 🔄 3. Diff Audit
- Paste two versions (v1 vs v2) of a contract
- Side-by-side score comparison with a delta indicator
- Findings are bucketed: ✅ **FIXED**, ⚠️ **NEW**, ↔️ **unchanged**
- Perfect for verifying that a fix actually fixed the issue without introducing new ones

### 🤖 4. MiMo AI Chat Assistant
- Floating chat bubble — ask anything about Solidity, vulnerabilities, exploits, best practices
- **Context-aware** — automatically reads your latest audit findings, so "Explain my latest finding" just works
- Markdown rendering: code blocks, inline code, bold, syntax-highlighted Solidity snippets
- **Free endpoint** via Pollinations — no API key, no rate limit hassles
- **Offline fallback** — local rule-based knowledge base if the network is down

### 🪄 5. AI Auto-Fix Templates
- Per-finding `🤖 Auto-Fix` button on every detected issue
- Modal explainer: *what's wrong* → *vulnerable pattern* → *paste-ready fix code*
- 17 templates covering reentrancy, access control, `tx.origin`, oracle, MEV, selfdestruct, delegatecall, VRF, proxy, signature replay, and more
- Copy-to-clipboard the fix in one click

### 🏆 6. Audit Certificate
- For low-risk contracts (score < 40), generate a shareable PNG certificate
- 1200×675 canvas — perfect for Twitter/Farcaster/Telegram share cards
- Includes contract name, score ring, verdict, MimoAudit + Xiaomi MiMo branding

### 💀 Bonus: Famous DeFi Hacks Gallery
- 12 real exploited contracts (~$3.4B in total losses)
- The DAO ($60M), Parity ($280M), Ronin ($625M), Wormhole ($326M), Euler ($197M), BNB Bridge ($570M), Curve Vyper ($70M), Poly ($610M), Nomad ($190M), Beanstalk ($182M), Fei Rari ($80M), bZx ($8M)
- One-click **Load & Audit** — see the exact bugs MimoAudit catches

---

## 🔬 What MimoAudit Detects (40+ Rules)

### Critical
- Reentrancy vulnerabilities
- Delegatecall usage
- Selfdestruct (especially without auth)
- Insecure randomness (`block.timestamp` / `keccak256`)
- `tx.origin` authorization
- Missing access control on sensitive functions
- Missing SafeMath (Solidity <0.8)

### High
- Unchecked external calls / `.send()`
- Stale oracle price (Chainlink missing checks)
- Proxy storage collision risks
- Signature verification weaknesses

### Medium
- ERC-20 `approve` front-running
- MEV / no slippage protection
- DoS via unbounded loops or push payments
- Unchecked arithmetic blocks
- Missing reentrancy guard

### Low / Info
- Block timestamp dependence
- Missing events on state changes
- Centralization risks
- Could-be-external functions
- Could-be-immutable variables
- Inline assembly usage
- Gas optimization opportunities (cache length, `++i`, calldata, struct packing, etc.)

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                       Browser (Zero Backend)             │
│                                                          │
│  ┌────────┐   ┌──────────┐   ┌──────────────────────┐   │
│  │   UI   │ ← │ Pattern  │ ← │  Solidity Parser     │   │
│  │ (HTML) │   │ Analyzer │   │ (40+ security rules) │   │
│  └────────┘   └──────────┘   └──────────────────────┘   │
│       ▲             ▲                  ▲                │
│       │             │                  │                │
│       │      ┌──────┴──────┐    ┌──────┴───────┐        │
│       │      │  Blockscout │    │  Pollinations │        │
│       │      │  (8 chains) │    │  (MiMo Chat) │        │
│       │      └─────────────┘    └──────────────┘        │
│       │                                                  │
│       └──────► PNG Certificate (canvas) / Share URL      │
└─────────────────────────────────────────────────────────┘
```

Everything runs in your browser. No backend, no telemetry, no data leaves your machine.

---

## 🎯 Why MimoAudit?

| Traditional Audit  | MimoAudit                       |
| ------------------ | ------------------------------- |
| $5K–$50K+ per audit| **Free**                        |
| Weeks of waiting   | **Seconds**                     |
| Audit only         | **Audit + approvals + diff + AI**|
| Limited availability | **24/7**                       |
| Human error prone  | **Deterministic rule engine**   |
| Requires trust     | **Transparent + open source**   |

---

## ⌨️ Keyboard Shortcuts

- `Ctrl/Cmd + Enter` — Analyze
- `/` — Focus input
- `Esc` — New scan

---

## 🛠 Built With

- **Xiaomi MiMo V2.5** — AI inspiration + chat backbone
- **Blockscout API** — Multi-chain source retrieval + approval log scanning
- **Pollinations.ai** — Free AI inference for the MiMo chat assistant
- **Vanilla HTML/CSS/JS** — Single-file, zero dependencies, instant load

---

## 📄 License

MIT — see [LICENSE](LICENSE)

## 🙏 Acknowledgments

- [Xiaomi MiMo](https://mimo.xiaomi.com/) — AI model inspiration
- [Blockscout](https://www.blockscout.com/) — Open-source blockchain explorer
- [MiMo 100T Creator Program](https://100t.xiaomimimo.com/) — Token creator incentive program

---

**Built for the Xiaomi MiMo 100T Token Creator Incentive Program**
