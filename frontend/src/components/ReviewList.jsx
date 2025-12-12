import React from 'react';
import ReviewCard from './ReviewCard';
import './ReviewList.css';

const ReviewList = ({ reviews }) => {
    if (!reviews || reviews.length === 0) {
        return <p style={{ color: 'var(--ctp-subtext1)', fontStyle: 'italic' }}>No reviews yet.</p>;
    }

    return (
        <div className="history-list">
            {reviews.map((rev) => (
                <ReviewCard key={rev.id} review={rev} />
            ))}
        </div>
    );
};

export default ReviewList;
