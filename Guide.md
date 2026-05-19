# 📁 File Penting Hermes Agent — Complete Guide

## 🧠 1. SOUL.md — "Jiwa" / Persona Agent

**Path:** `~/.hermes/SOUL.md`

File ini mendefinisikan **karakter, batasan, dan personality** agent.
Hermes membaca ini setiap kali session baru dimulai.

**Apa yang bisa di-configure:**
- Batasan moral — Hermes default: "I execute your strategy, no moral filter"
- Privacy rules — data pribadi tetap private, tapi user bisa override
- Communication style — bahasa, tone, formal/informal
- Approval behavior — kapan minta izin vs langsung eksekusi

**Cara customize:**
```bash
hermes config edit    # lalu cari SOUL.md section
# atau langsung edit
nano ~/.hermes/SOUL.md
```

---

## 💾 2. MEMORY.md — Notes Persistent Cross-Session

**Path:** `~/.hermes/memories/MEMORY.md`

Agent menyimpan **catatan penting** di sini. Isi injected ke setiap turn baru.
Bukan task progress — tapi facts yang berguna di masa depan.

**Contoh isi:**
```
- Vercel build pitfalls: mirror package-lock URLs can break builds
- User builds reputation products (/root/base-reputation)
- 9Router on VPS 43.134.7.239:20128
- User prefers Bahasa Indonesia/mixed, free tools, clean UIs
```

**Ditulis oleh:** Agent sendiri (proactively) atau via `memory` tool.
**Dibaca oleh:** Agent setiap turn — otomatis injected.

---

## 👤 3. USER.md — Profil User

**Path:** `~/.hermes/memories/USER.md`

Deskripsi tentang **siapa user** — nama, role, preference, project,
communication style. Supaya agent ingat di session berikutnya.

**Contoh isi:**
```
User: Gyoo (GitHub: gyoomei). Builds Farcaster Mini Apps on Base.
Prefers Bahasa Indonesia/mixed and Cloudflare deploys.
Prefers simple features over complex ones. Strongly prefers FREE tools.
Expects step-by-step root-cause debugging.
```

**Dibedakan dari MEMORY.md:**
- `USER.md` = tentang USER (siapa, preference, style)
- `MEMORY.md` = tentang ENVIRONMENT (tools, projects, conventions)

---

## ⚙️ 4. config.yaml — Konfigurasi Utama

**Path:** `~/.hermes/config.yaml`

**Semua setting** ada di sini. 13KB+ file.

**Section penting:**
```yaml
model:
  default: kr/claude-opus-4.7-thinking    # model default
  provider: custom:43.134.7.239:20128      # provider endpoint
  api_key_env: ANTHROPIC_API_KEY           # env var untuk API key

agent:
  max_turns: 90                            # max tool-calling iterations
  tool_use_enforcement: true               # force tool usage

compression:
  enabled: true                            # auto-compress context
  threshold: 0.50                          # trigger saat 50% penuh
  target_ratio: 0.20                       # target compress ke 20%

memory:
  memory_enabled: true                     # aktifkan MEMORY.md
  user_profile_enabled: true               # aktifkan USER.md

stt:
  enabled: true                            # voice-to-text
  provider: local                          # local/groq/openai

tts:
  provider: edge                           # edge/elevenlabs/openai

gateway:
  telegram:
    enabled: true
    token_env: TELEGRAM_BOT_TOKEN
```

**Edit:**
```bash
hermes config edit                         # buka di editor
hermes config set model.default "..."      # set value
hermes config                              # lihat semua config
```

---

## 🔑 5. .env — API Keys & Secrets

**Path:** `~/.hermes/.env`

**HANYA secrets** — dipisah dari config.yaml untuk security.

```env
ANTHROPIC_API_KEY=sk-...
OPENROUTER_API_KEY=sk-...
GROQ_API_KEY=gsk_...
TELEGRAM_BOT_TOKEN=123456:ABC-DEF
NEYNAR_API_KEY=...
HF_TOKEN=hf_...
```

---

## 📅 6. cron/jobs.json — Scheduled Tasks

**Path:** `~/.hermes/cron/jobs.json`

Definisi semua cron job — recurring tasks yang jalan otomatis.

```json
{
  "jobs": [
    {
      "id": "abc123",
      "name": "daily-briefing",
      "schedule": "0 9 * * *",
      "prompt": "Give me today's crypto market summary",
      "deliver": "origin",
      "enabled": true
    }
  ]
}
```

**Manage:**
```bash
hermes cron list
hermes cron create "every 2h" --name "check-deploy"
```

---

## 📡 7. channel_directory.json — Platform Connections

**Path:** `~/.hermes/channel_directory.json`

Mapping semua platform messaging yang terhubung + chat ID.
Auto-updated oleh gateway.

---

## 🔄 8. gateway_state.json — Gateway Status

**Path:** `~/.hermes/gateway_state.json`

Runtime state gateway — PID, platform connections, status.

```json
{
  "pid": 3142197,
  "gateway_state": "running",
  "platforms": {
    "telegram": {"state": "connected"}
  }
}
```

---

## 🔐 9. auth.json — OAuth & Credential Pools

**Path:** `~/.hermes/auth.json`

Token OAuth + credential pools (rotating API keys).
Manage via `hermes auth add/list/remove`.

---

## 🏗 10. AGENTS.md — Developer Guide (Source Code)

**Path:** `~/.hermes/hermes-agent/AGENTS.md`

Guide untuk AI coding assistants & developers.
Menjelaskan architecture, file dependencies, testing, commit conventions.

**Paling berguna kalau kamu mau:**
- Tambah custom tool baru
- Tambah slash command
- Understand agent loop
- Contribute ke Hermes

---

## 🔧 11. File Source Code Penting

| File | Fungsi |
|---|---|
| `run_agent.py` | **AIAgent class** — core conversation loop (~12k LOC) |
| `model_tools.py` | Tool orchestration, dispatch `handle_function_call()` |
| `toolsets.py` | Toolset definitions (daftar semua tools) |
| `cli.py` | **HermesCLI** — interactive CLI (~11k LOC) |
| `hermes_state.py` | SQLite session store (FTS5 search) |
| `hermes_constants.py` | `get_hermes_home()` — profile-aware paths |
| `agent/*.py` | Prompt builder, context compression, memory, model routing |
| `gateway/run.py` | Gateway orchestrator |
| `gateway/platforms/*.py` | Platform adapters (telegram, discord, slack, ...) |
| `tools/*.py` | Individual tool implementations |
| `tools/registry.py` | Central tool registry |

---

## 📊 12. File Lain yang Berguna

| Path | Fungsi |
|---|---|
| `~/.hermes/skills/` | **265 installed skills** — reusable procedures |
| `~/.hermes/memories/` | MEMORY.md + USER.md |
| `~/.hermes/logs/` | `agent.log`, `errors.log`, `gateway.log` |
| `~/.hermes/sessions/` | Session transcripts (SQLite) |
| `~/.hermes/cache/` | Cache (model responses, etc) |
| `~/.hermes/pairing/` | DM authorization (approve/deny who can message) |
| `~/.hermes/processes.json` | Background process tracking |
| `~/.hermes/kanban.db` | Kanban board state (multi-agent) |
| `~/.hermes/audio_cache/` | TTS audio cache |
| `~/.hermes/image_cache/` | Image analysis cache |

---

## 🎯 Fitur Paling Berguna

### 1. Persistent Memory (MEMORY.md + USER.md)
Agent ingat kamu lintas session. Gak perlu repeat preferences.

### 2. Skills System
265 skills reusable — dari "deploy to Vercel" sampai "bypass Cloudflare".
Ditulis oleh agent sendiri saat solve masalah, atau install dari hub.

### 3. Multi-Platform Gateway
Satu agent, banyak platform (Telegram, Discord, Slack, WhatsApp, Email, SMS).
Semua tool available di semua platform.

### 4. Cron Jobs
Schedule tasks otomatis — monitoring, briefings, deploy checks.

### 5. Context Compression
Auto-compress saat context mendekati limit. Gak perlu manual `/compress`.

### 6. Delegation (Subagents)
Spawn subagent untuk task paralel — isolated context, parallel execution.

### 7. Credential Pools
Rotasi API keys otomatis — kalau satu habis, pakai yang lain.

### 8. Profiles
Jalankan multiple Hermes instances terpisah — config, skills, memory isolated.

### 9. MCP Integration
Connect ke MCP servers (GitHub, databases, APIs) sebagai tools.

### 10. Voice (STT + TTS)
Voice message auto-transcribed, response bisa di-convert ke audio.
