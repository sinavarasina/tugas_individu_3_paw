from sqlalchemy import Column, Integer, String, Text, Float
from .base import Base


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False, index=True)
    review_text = Column(Text, nullable=False)
    sentiment = Column(String(50))
    score = Column(String(50))
    key_points = Column(Text)
