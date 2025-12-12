from pydantic import BaseModel, Field


class ReviewCreateSchema(BaseModel):
    product_name: str = Field(..., min_length=2)
    review_text: str = Field(..., min_length=3)
