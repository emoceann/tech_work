from fastapi import FastAPI
from app.questions.api import router as questions_router

app = FastAPI(debug=True)
app.include_router(questions_router)
