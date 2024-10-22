import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios'; 
import './FoodRecognitionPage.css'; 

const FoodRecognitionPage = () => {
  const [preview, setPreview] = useState('https://www.researchgate.net/publication/339245946/figure/fig3/AS:858286853206017@1581642940296/The-automatic-three-steps-system-of-food-recognition-and-nutrition-analysis-system.ppm');
  const [errorMessage, setErrorMessage] = useState(''); 
  const navigate = useNavigate(); 

  const displayImage = async (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = () => {
      setPreview(reader.result); 
    };

    if (file) {
      reader.readAsDataURL(file);

      const formData = new FormData();
      // Changing the key from 'file' to 'image'
      formData.append('image', file);

      try {
        const response = await axios.post('http://127.0.0.1:7766/api/upload_image', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        if (response.status === 200) {
          const data = response.data;

          navigate('/results', {
            state: { foodType: data.food_name, calories: data.calories, previewImage: reader.result },
          });
        } else {
          setErrorMessage('Image upload failed!! Please upload and identify again'); 
        }
      } catch (error) {
        setErrorMessage('Image upload failed!! Please upload and identify again'); 
      }
    }
  };

  const retryUpload = () => {
    setPreview('https://www.researchgate.net/publication/339245946/figure/fig3/AS:858286853206017@1581642940296/The-automatic-three-steps-system-of-food-recognition-and-nutrition-analysis-system.ppm');
    setErrorMessage(''); 

    const fileInput = document.getElementById('file-input');
    fileInput.value = ''; 
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
          <button onClick={retryUpload}>Retry</button>
        </div>
      )}
    </div>
  );
};

export default FoodRecognitionPage;


