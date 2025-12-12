import React from 'react';
import './ReviewCard.css';

const ReviewCard = ({ review }) => {
    const { product_name, sentiment, score, review_text, key_points } = review;

    return (
        <div className={`review-card border-${sentiment}`}>
            <div className="card-header">
                <span className="product-name">{product_name}</span>
                <span>
                    {sentiment} ({parseFloat(score).toFixed(2)})
                </span>
            </div>

            <div className="review-text">"{review_text}"</div>

            <div className="ai-points">
                <pre>{key_points}</pre>
            </div>
        </div>
    );
};

export default ReviewCard;
