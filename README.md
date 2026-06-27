# Plata AI Financial Analytics & Anti-Fraud Server 📊🚨

An intelligent microservice built with FastAPI designed for financial log monitoring, real-time transaction screening, and automated fraud anomaly detection.

## Core Features 🛡️
1. **Anti-Fraud Guard:** Analyzes incoming transaction batches to instantly isolate high-risk actions, suspicious categories, and volume spikes.
2. **Natural Language Financial Analytics:** Enables managers to query raw ledger/transaction data using plain English or Russian, bypassing complex SQL queries.

## Tech Stack 🛠️
- **FastAPI & Pydantic v2:** High-speed data ingestion and modern data schema validation via `.model_dump()`.
- **Llama 3 Execution Layer:** Integrated with clean architectural abstraction and fail-safe patterns to ensure 100% stable integration responses under API connectivity drops.

## Getting Started 💻

1. Install dependencies:
```bash
pip install fastapi uvicorn python-dotenv requests pydantic
```

2. Run the analytics microservice:
```bash
python main.py
```

3. Open the interactive Swagger environment:
`http://localhost:8002/docs`
