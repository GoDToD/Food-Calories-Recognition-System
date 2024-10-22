import React from 'react';
import { Link } from 'react-router-dom';
import './MainPage.css'; 

const MainPage = () => {
  return (
    <div>
      <header>Intelligent Food Calorie Recognition System</header>
      <div className="container">
        <div className="main-content">
          <h1>Welcome to the Intelligent Food Calorie Tracking Tool</h1>
          <p>
            By taking a photo of your food, our system can automatically recognize the food type and estimate its
            calories. Make your health management easy and convenient!
          </p>
          <Link to="/food-recognition" className="upload-btn">
            Click Here to Start Your New Life
          </Link>
        </div>
        <section className="business-value">
          <h2>Business Value Overview</h2>
          <p>
            This system is not only suitable for personal health management, but also has broad applications in the
            food service industry, nutrition consultation, and more, helping businesses and individuals better manage diet and health.
          </p>
        </section>
      </div>
      <footer>&copy; 2024 Intelligent Food Calorie Recognition System | Designed by NUS-ISS-Group 18.</footer>
    </div>
  );
};

export default MainPage;
