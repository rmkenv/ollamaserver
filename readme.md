# Sovereign Server — Private AI Agent Hub

[![Python](https://img.shields.io/badge/Python-3.14-blue)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-local-green)](https://ollama.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-teal)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-GUI-red)](https://streamlit.io)

Turn an old Windows PC into a private, always-on AI agent server using Ollama.

- No cloud subscriptions
- No data leaving your machine
- Remote access with Tailscale
- Optional Wake-on-LAN support
- Windows services via NSSM

Source article:
[The Sovereign Server - Build Your Own Private AI Agent Hub](https://ryankmetz.substack.com/p/the-sovereign-server-build-your-own)

## What this repo includes

- `agent.py` — FastAPI backend for local LLM requests
- `chat.py` — Streamlit multi-agent UI
- `setup.ps1` — setup helper for Windows
- `nssm/install_services.ps1` — register backend and UI as services
- `docs/tailscale_wol.md` — remote access notes
- `.github/workflows/lint.yml` — CI lint check

## Hardware

| Component | Minimum | Recommended |
|---|---|---|
| RAM | 8 GB | 16 GB+ |
| CPU | i5 4th Gen | i5 7th Gen+ |
| Storage | 100 GB | SSD preferred |
| Network | Ethernet for reliable WoL | Ethernet |

## Quick start

### 1. Install Python and Ollama

```powershell
winget install Python.Python.3.14
python --version
winget install Ollama.Ollama
ollama serve
```

### 2. Pull local models

```powershell
ollama pull llama3.2:3b
ollama pull qwen2.5:3b
```

### 3. Clone repo and install dependencies

```powershell
git clone https://github.com/rmkenv/sovereign-server.git
cd sovereign-server
pip install -r requirements.txt
```

### 4. Start backend

```powershell
uvicorn agent:app --host 0.0.0.0 --port 8000
```

### 5. Start Streamlit UI

```powershell
streamlit run chat.py --server.headless true --server.address 0.0.0.0 --server.port 8501
```

Then open:

```text
http://localhost:8501
```

## Remote access

Install Tailscale:

```powershell
winget install Tailscale.Tailscale
tailscale up
tailscale ip -4
```

Then access:

```text
http://[tailscale-ip]:8501
```

## Windows services

Install NSSM:

```powershell
winget install NSSM.NSSM
```

Then run:

```powershell
.\nssm\install_services.ps1
```

## Notes

This project is based on a Windows workflow using Ollama, FastAPI, Streamlit, NSSM, Tailscale, and Wake-on-LAN. The article also estimates idle power use around 30–50 W and compares that with a cloud GPU instance around 150 W continuous. [page:2]
