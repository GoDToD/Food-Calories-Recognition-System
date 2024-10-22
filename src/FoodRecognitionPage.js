// src/components/FoodRecognitionPage.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios'; // 引入 Axios
import './FoodRecognitionPage.css'; // 引入CSS文件

const FoodRecognitionPage = () => {
  const [preview, setPreview] = useState('https://www.researchgate.net/publication/339245946/figure/fig3/AS:858286853206017@1581642940296/The-automatic-three-steps-system-of-food-recognition-and-nutrition-analysis-system.ppm');
  const [errorMessage, setErrorMessage] = useState(''); // 新增状态管理错误信息
  const navigate = useNavigate(); // 使用useNavigate

  const displayImage = async (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = () => {
      setPreview(reader.result);
    };

    if (file) {
      reader.readAsDataURL(file);

      // 发送图片到后端
      const formData = new FormData();
      formData.append('file', file);

      try {
        const response = await axios.post('http://localhost:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        if (response.status === 200) {
          const data = response.data;

          // 跳转到结果页面，并传递识别结果
          navigate('/results', {
            state: { foodType: data.foodType, calories: data.calories, nutritionInfo: data.nutritionInfo },
          });
        } else {
          setErrorMessage('Error uploading file: ' + response.statusText); // 设置错误消息
        }
      } catch (error) {
        setErrorMessage('Error: ' + error.message); // 设置错误消息
      }
    }
  };

  const resetUpload = () => {
    setPreview('https://www.researchgate.net/publication/339245946/figure/fig3/AS:858286853206017@1581642940296/The-automatic-three-steps-system-of-food-recognition-and-nutrition-analysis-system.ppm');
    setErrorMessage(''); // 清空错误消息
  };

  return (
    <div className="container">
      <header>
        <h1>Food Recognition System</h1>
        <p>Upload an image of your food to estimate its calories</p>
      </header>
      <div className="upload-section">
        <label htmlFor="file-input" className="upload-label">
          <i className="fas fa-camera"></i>
          Click Here to Upload Image
        </label>
        <input type="file" id="file-input" accept="image/*" onChange={displayImage} />
        <img id="preview" className="preview-image" src={preview} alt="Image Preview" />
      </div>
      {errorMessage && (
        <div className="error-message">
          <p>{errorMessage}</p>
          <button onClick={resetUpload}>Re-upload</button>
        </div>
      )}
    </div>
  );
};

export default FoodRecognitionPage;
