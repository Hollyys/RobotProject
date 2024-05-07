import React, { useState } from 'react';
import image from './knu.png';
import './App.css';

function App() {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setSelectedImage(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <div style={{ marginBottom: '10px' }}>
          <img src={image} width="600px" alt="KNU Logo" />
        </div>
        <p>
          모바일 로봇 프로그래밍 중간과제
        </p>
        {selectedImage && (
          <img src={selectedImage} alt="Uploaded" style={{ width: '800px', marginTop: '20px' }} />
        )}
        <div style={{ marginTop: '10px' }}>
          <input type="file" onChange={handleImageChange} />
        </div>
        <a
          className="App-link"
          href="https://github.com/Hollyys/RobotProject.git"
          target="_blank"
          rel="noopener noreferrer"
          style={{ marginTop: '10px', display: 'block' }}
        >
          git repository
        </a>
      </header>
    </div>
  );
}

export default App;
