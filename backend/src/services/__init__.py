from .review_service import ReviewService


class ServiceContainer:
    def __init__(self, session):
        self.session = session
        self.review = ReviewService(session)
