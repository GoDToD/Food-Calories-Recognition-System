import React, { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import './ResultsPage.css';
import Chart from 'chart.js/auto';
import axios from 'axios'; 

const ResultsPage = () => {
  const { state } = useLocation();
  const { foodType, calories, nutritionInfo } = state;

  const { carbohydrates, protein, fat } = nutritionInfo; 

  useEffect(() => {
    const ctx = document.getElementById('nutritionChart').getContext('2d');
    const nutritionData = {
      labels: ['Carbohydrates', 'Protein', 'Fat'], 
      datasets: [{
        label: 'Nutritional Breakdown',
        data: [carbohydrates, protein, fat], 
        backgroundColor: ['#ff6384', '#36a2eb', '#ffce56'],
        hoverBackgroundColor: ['#ff6384', '#36a2eb', '#ffce56'],
      }],
    };

  
    new Chart(ctx, {
      type: 'pie', 
      data: nutritionData,
    });
  }, [nutritionInfo]);

  const getDietarySuggestions = async () => {
    try {
      const response = await axios.post('http://localhost:5000/get-suggestions', {
        calories,
      });

      const data = response.data;
      alert(data.suggestions);
    } catch (error) {
      console.error('Error fetching suggestions:', error);
    }
  };

  return (
    <div className="results-container">
      <h2>Food Recognition Results</h2>
      <h3>Food Item: {foodType}</h3>
      <p>Estimated Calories: {calories} kcal</p>
      <p>Nutritional Information: {JSON.stringify(nutritionInfo)}</p> 
      <canvas id="nutritionChart" width="200" height="200"></canvas> }
      <button onClick={getDietarySuggestions}>Get Dietary Suggestions</button>
    </div>
  );
};

export default ResultsPage;

