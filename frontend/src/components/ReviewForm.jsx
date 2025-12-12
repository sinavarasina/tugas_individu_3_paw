import React, { useState } from 'react';
import './ReviewForm.css';

const ReviewForm = ({ onAnalyze, loading }) => {
    const [formData, setFormData] = useState({
        product_name: '',
        review_text: '',
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onAnalyze(formData, () => {
            setFormData({ product_name: '', review_text: '' });
        });
    };

    return (
        <form onSubmit={handleSubmit} className="review-form">
            <input
                type="text"
                name="product_name"
                placeholder="PRODUCT NAME"
                value={formData.product_name}
                onChange={handleChange}
                required
                disabled={loading}
            />
            <textarea
                name="review_text"
                placeholder="WRITE YOUR REVIEW HERE..."
                rows="4"
                value={formData.review_text}
                onChange={handleChange}
                required
                disabled={loading}
            />
            <button type="submit" disabled={loading}>
                {loading ? 'ANALYZING...' : 'ANALYZE'}
            </button>
        </form>
    );
};

export default ReviewForm;
