# Plata AI HR Automation System 🤖💼

Multi-agent AI ecosystem designed to automate candidate screening, CV analysis, and technical interview design. Built with FastAPI and structured LLM agent chains.

## How It Works ⚙️
1. **Agent 1 (CV Screener):** Evaluates candidate resumes against complex job descriptions, identifying key strengths and critical skills gaps.
2. **Agent 2 (Interview Designer):** Reviews the CV Screener's analysis and dynamically generates 3-5 hyper-targeted, tough technical interview questions to test the candidate's exact weaknesses.

## Tech Stack 🛠️
- **FastAPI:** Clean, asynchronous web routing layer.
- **LangChain Core Concepts:** Sequential agent orchestration and prompt routing.
- **Llama 3 (via OpenRouter):** Advanced open-source language model serving as the brain for both specialized agents.

## Getting Started 💻

1. Install dependencies:
```bash
pip install fastapi uvicorn python-dotenv langchain-core requests
```

2. Run the server:
```bash
python main.py
```

3. Explore interactive Swagger documentation:
`http://localhost:8001/docs`
