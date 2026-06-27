from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from analytics_engine import analytics_engine

app = FastAPI(
    title="Plata AI Financial Analytics Server",
    description="Интеллектуальная система мониторинга транзакций и Anti-Fraud контроля",
    version="1.0.0"
)

# Структура одной транзакции для валидации через Pydantic
class Transaction(BaseModel):
    id: int
    user_id: int
    amount: float
    category: str
    description: str

# Структура входящего запроса
class AnalyticsRequest(BaseModel):
    transactions: List[Transaction]
    query: str

@app.get("/")
async def root():
    return {"status": "online", "message": "Financial Guard AI готов к анализу данных"}

@app.post("/analyze")
async def analyze_data(request: AnalyticsRequest):
    """Эндпоинт агрегирует данные и запускает ИИ-анализ логов/транзакций"""
    if not request.transactions:
        raise HTTPException(status_code=400, detail="Список транзакций не может быть пустым.")
    
    try:
        # Превращаем объекты Pydantic в обычные словари для движка
        txns_list = [t.model_dump() for t in request.transactions]
        report = analytics_engine.analyze_transactions(txns_list, request.query)
        return {
            "manager_query": request.query,
            "total_processed": len(txns_list),
            "ai_report": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Запускаем на порту 8002 с исправленным синтаксисом хоста
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)
