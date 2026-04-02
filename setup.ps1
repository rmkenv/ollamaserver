Write-Host "=== Sovereign Server Setup ===" -ForegroundColor Cyan

Write-Host "`n[1/5] Installing Python..." -ForegroundColor Yellow
winget install Python.Python.3.14 --accept-source-agreements --accept-package-agreements

Write-Host "`n[2/5] Installing Ollama..." -ForegroundColor Yellow
winget install Ollama.Ollama --accept-source-agreements --accept-package-agreements

Write-Host "`n[3/5] Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host "`n[4/5] Pulling models..." -ForegroundColor Yellow
ollama pull llama3.2:3b
ollama pull qwen2.5:3b

Write-Host "`n[5/5] Installing NSSM..." -ForegroundColor Yellow
winget install NSSM.NSSM --accept-source-agreements --accept-package-agreements

Write-Host "`nSetup complete." -ForegroundColor Green
Write-Host "Run backend: uvicorn agent:app --host 0.0.0.0 --port 8000"
Write-Host "Run UI: streamlit run chat.py --server.headless true --server.address 0.0.0.0 --server.port 8501"
