import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './ResultsPage.css';

const ResultsPage = () => {
  const { state } = useLocation();
  const { foodType, calories, previewImage } = state;
  const navigate = useNavigate();

  const handleRetry = () => {
    navigate('/'); 
  };

  return (
    <div className="results-container">
      <h2>Food Recognition Results</h2>
      <img src={previewImage} alt="Uploaded Food" className="result-image" />
      <h3>Food Item: {foodType}</h3>
      <p>Estimated Calories: {calories} kcal/100g</p>

      <div className="button-container">
        <button className="retry-button" onClick={handleRetry}>
          Retry Upload
        </button>
      </div>

      <div className="footer">
        <p>Note: Calorie estimates are based on standard serving sizes.</p>
      </div>
    </div>
  );
};

export default ResultsPage;


