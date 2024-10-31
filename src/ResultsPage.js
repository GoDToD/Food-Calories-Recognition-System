// ResultsPage.js
import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './ResultsPage.css';

const ResultsPage = () => {
  const { state } = useLocation();
  const { results, previewImage } = state;
  const navigate = useNavigate();

  const handleRetry = () => {
    navigate('/');
  };

  return (
    <div className="results-container">
      <h2>Food Recognition Results</h2>
      <img src={previewImage} alt="Uploaded Food" className="result-image" />
      
      {results.map((result, index) => (
        <div key={index} className="result-item">
          <h3>Food Item: {result.food_name}</h3>
          <p>Estimated Calories: {result.calories} kcal/100g</p>
        </div>
      ))}

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

