from pyramid.view import view_config
from src.schemas import ReviewCreateSchema


@view_config(route_name='analyze_review', request_method='POST', renderer='json')
def analyze_review(request):
    try:
        payload = ReviewCreateSchema(**request.json_body)
    except Exception as e:
        request.response.status_code = 400
        return {"error": str(e)}

    review = request.services.review.analyze_and_create(
        product_name=payload.product_name,
        review_text=payload.review_text
    )

    request.response.status_code = 201
    return review


@view_config(route_name='get_reviews', request_method='GET', renderer='json')
def get_reviews(request):
    return request.services.review.get_all()
