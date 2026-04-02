import streamlit as st
import requests

st.set_page_config(
    page_title="Sovereign Server",
    page_icon="🤖",
    layout="wide"
)

AGENT_URL = "http://localhost:8000/agent"
MODELS = ["llama3.2:3b", "qwen2.5:3b"]

if "agents" not in st.session_state:
    st.session_state.agents = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_agent" not in st.session_state:
    st.session_state.selected_agent = None

st.title("🤖 Local AI Agent Hub")

with st.sidebar.form("new_agent"):
    st.subheader("Create Agent")
    name = st.text_input("Agent Name")
    model = st.selectbox("Model", MODELS)
    instructions = st.text_area("Instructions")
    created = st.form_submit_button("Create Agent")

    if created and name.strip():
        st.session_state.agents.append({
            "name": name.strip(),
            "model": model,
            "instructions": instructions.strip() or "You are a helpful local AI assistant."
        })
        st.session_state.selected_agent = name.strip()
        st.session_state.messages = []
        st.rerun()

if st.session_state.agents:
    names = [a["name"] for a in st.session_state.agents]
    selected = st.sidebar.selectbox("Select Agent", names)
    agent = next(a for a in st.session_state.agents if a["name"] == selected)
    st.session_state.selected_agent = selected

    st.sidebar.markdown(f"**Model:** `{agent['model']}`")
    st.sidebar.write(agent["instructions"])

    if st.sidebar.button("Delete Agent"):
        st.session_state.agents = [a for a in st.session_state.agents if a["name"] != selected]
        st.session_state.messages = []
        st.session_state.selected_agent = None
        st.rerun()
else:
    st.info("Create an agent in the sidebar to begin.")
    st.stop()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask your local AI agent...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    payload = {
        "task": prompt,
        "model": agent["model"],
        "system_prompt": agent["instructions"]
    }

    try:
        r = requests.post(AGENT_URL, json=payload, timeout=120)
        r.raise_for_status()
        reply = r.json()["response"]
    except Exception as e:
        reply = f"Error contacting backend: {e}"

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
