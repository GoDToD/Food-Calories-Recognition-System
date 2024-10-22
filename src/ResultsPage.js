// src/components/ResultsPage.js
import React, { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import './ResultsPage.css';
import Chart from 'chart.js/auto';
import axios from 'axios'; // 引入 Axios

const ResultsPage = () => {
  const { state } = useLocation();
  const { foodType, calories, nutritionInfo } = state;

  // 假设 nutritionInfo 是一个对象，其中包含各个营养成分
  const { carbohydrates, protein, fat } = nutritionInfo; // 从 nutritionInfo 中提取各个成分

  useEffect(() => {
    const ctx = document.getElementById('nutritionChart').getContext('2d');
    const nutritionData = {
      labels: ['Carbohydrates', 'Protein', 'Fat'], // 根据 nutritional info 填充
      datasets: [{
        label: 'Nutritional Breakdown',
        data: [carbohydrates, protein, fat], // 使用从 nutritionInfo 中提取的数据
        backgroundColor: ['#ff6384', '#36a2eb', '#ffce56'],
        hoverBackgroundColor: ['#ff6384', '#36a2eb', '#ffce56'],
      }],
    };

    // 初始化饼图
    new Chart(ctx, {
      type: 'pie', // 使用饼图
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
      <p>Nutritional Information: {JSON.stringify(nutritionInfo)}</p> {/* 可以更好地格式化显示营养信息 */}
      <canvas id="nutritionChart" width="200" height="200"></canvas> {/* 修改宽度和高度 */}
      <button onClick={getDietarySuggestions}>Get Dietary Suggestions</button>
    </div>
  );
};

export default ResultsPage;

