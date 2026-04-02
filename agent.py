from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama

app = FastAPI(
    title="Sovereign Server API",
    description="Local Ollama-backed AI agent API",
    version="1.0.0"
)

ALLOWED_MODELS = ["llama3.2:3b", "qwen2.5:3b"]

class Task(BaseModel):
    task: str
    model: str = "llama3.2:3b"
    system_prompt: str = "You are a helpful local AI assistant."

@app.get("/")
def root():
    return {"status": "ok", "message": "Sovereign Server is running"}

@app.get("/health")
def health():
    try:
        ollama.list()
        return {"status": "healthy"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

@app.get("/models")
def models():
    try:
        data = ollama.list()
        return {"models": [m["name"] for m in data.get("models", [])]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/agent")
def run_agent(task: Task):
    if task.model not in ALLOWED_MODELS:
        raise HTTPException(
            status_code=400,
            detail=f"Model '{task.model}' not allowed. Allowed: {ALLOWED_MODELS}"
        )

    try:
        response = ollama.chat(
            model=task.model,
            messages=[
                {"role": "system", "content": task.system_prompt},
                {"role": "user", "content": task.task}
            ]
        )
        return {
            "response": response["message"]["content"],
            "model": task.model
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
