import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

import ReviewForm from './components/ReviewForm';
import ReviewList from './components/ReviewList';

const API_URL = "http://localhost:6543/api";

function App() {
    const [reviews, setReviews] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        fetchReviews();
    }, []);

    const fetchReviews = async () => {
        try {
            const res = await axios.get(`${API_URL}/reviews`);
            setReviews(res.data);
        } catch (err) {
            console.error("Failed to fetch data", err);
        }
    };

    const handleAnalyze = async (data, onSuccess) => {
        setLoading(true);
        try {
            await axios.post(`${API_URL}/analyze-review`, data);
            fetchReviews();
            if (onSuccess) onSuccess();
        } catch (err) {
            alert("Failed to analyze. Make sure the backend is running.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="container">
            <h1>Review Analyzer</h1>

            {/* Form Component */}
            <ReviewForm onAnalyze={handleAnalyze} loading={loading} />

            {/* List Component */}
            <ReviewList reviews={reviews} />
        </div>
    );
}

export default App;
