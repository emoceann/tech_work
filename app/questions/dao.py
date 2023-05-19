from app.db.config import Base
from sqlalchemy import Column, BigInteger, String, DateTime


class Question(Base):
    __tablename__ = "question"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    question_id = Column(BigInteger, index=True)
    question = Column(String(1024))
    answer = Column(String(1024))
    created_at = Column(DateTime(timezone=True))




