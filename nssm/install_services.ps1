$RepoPath = Split-Path -Parent $PSScriptRoot
$PythonExe = "C:\Users\User\AppData\Local\Programs\Python\Python314\python.exe"

nssm install OllamaAgent $PythonExe "-m uvicorn agent:app --host 0.0.0.0 --port 8000"
nssm set OllamaAgent AppDirectory $RepoPath
nssm set OllamaAgent AppStdout "$RepoPath\agent.log"
nssm set OllamaAgent AppStderr "$RepoPath\agent-err.log"
nssm start OllamaAgent

nssm install StreamlitAgentHub $PythonExe "-m streamlit run chat.py --server.headless true --server.address 0.0.0.0 --server.port 8501"
nssm set StreamlitAgentHub AppDirectory $RepoPath
nssm set StreamlitAgentHub AppStdout "$RepoPath\streamlit.log"
nssm set StreamlitAgentHub AppStderr "$RepoPath\streamlit-err.log"
nssm start StreamlitAgentHub
