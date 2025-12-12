import os
import google.generativeai as genai
import torch
from transformers import pipeline
from src.models import Review
from src.utils import AppError


class ReviewService:
    def __init__(self, session):
        self.session = session

        self.gemini_key = os.getenv("GEMINI_API_KEY")
        if self.gemini_key:
            genai.configure(api_key=self.gemini_key)
            self.gemini_model = genai.GenerativeModel('gemini-1.5-flash')

        device_id = 0 if torch.cuda.is_available() else -1
        device_name = "CPU"
        if device_id == 0:
            device_name = torch.cuda.get_device_name(0)

        print(f"AI Service initialized on: {device_name}")

        self.sentiment_pipeline = pipeline(
            "sentiment-analysis",
            device=device_id
        )

    def get_all(self):
        return self.session.query(Review).order_by(Review.id.desc()).all()

    def analyze_and_create(self, product_name, review_text):
        try:
            hf_result = self.sentiment_pipeline(review_text)[0]
            sentiment_label = hf_result['label']
            sentiment_score = str(round(hf_result['score'], 4))

            key_points_text = "AI Not Configured"
            if self.gemini_key:
                prompt = f"Extract key points from this product review as a bulleted list. Keep it concise:\n\n{
                    review_text}"
                gemini_resp = self.gemini_model.generate_content(prompt)
                key_points_text = gemini_resp.text

            review = Review(
                product_name=product_name,
                review_text=review_text,
                sentiment=sentiment_label,
                score=sentiment_score,
                key_points=key_points_text
            )

            self.session.add(review)
            self.session.flush()
            return review

        except Exception as e:
            print(f"Error: {e}")
            raise AppError(f"Analysis failed: {str(e)}", status_code=500)
