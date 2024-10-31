// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import FoodRecognitionPage from './FoodRecognitionPage';
import ResultsPage from './ResultsPage'; // 导入结果页面组件

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/food-recognition" element={<FoodRecognitionPage />} />
        <Route path="/results" element={<ResultsPage />} /> {/* 添加结果页面的路由 */}
      </Routes>
    </Router>
  );
}

export default App;

