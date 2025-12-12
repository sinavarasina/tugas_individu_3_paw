import os
import google.generativeai as genai
import torch
from transformers import pipeline
from src.models import Review
from src.utils import AppError

_GLOBAL_SENTIMENT_PIPELINE = None


class ReviewService:

    def __init__(self, session):
        self.session = session

        self.gemini_key = os.getenv("GEMINI_API_KEY")
        if self.gemini_key:
            genai.configure(api_key=self.gemini_key)
            self.gemini_model = genai.GenerativeModel('gemini-2.5-flash')

        global _GLOBAL_SENTIMENT_PIPELINE

        if _GLOBAL_SENTIMENT_PIPELINE is None:
            device_id = 0 if torch.cuda.is_available() else -1
            model_name = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"

            print(f"Loading Model: {model_name}")

            _GLOBAL_SENTIMENT_PIPELINE = pipeline(
                "sentiment-analysis",
                model=model_name,
                device=device_id
            )

        self.sentiment_pipeline = _GLOBAL_SENTIMENT_PIPELINE

    def get_all(self):
        return self.session.query(Review).order_by(Review.id.desc()).all()

    def analyze_and_create(self, product_name, review_text):
        try:
            hf_result = self.sentiment_pipeline(review_text)[0]

            sentiment_label = hf_result['label'].upper()
            sentiment_score = str(round(hf_result['score'], 4))

            key_points_text = "AI Not Configured"
            if self.gemini_key:
                prompt = (
                    f"EN: Extract key points from this product review as a concise bulleted list. "
                    f"Please respond in the same language as the review\n\n"
                    f"ID: Ekstrak key point dari produk review ini dan buat list yang singkat."
                    f"Tolong jawab dengan bahasa yang sama dengan bahasa yang digunakan di review\n\n"
                    f"Review: {review_text}"
                )
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
