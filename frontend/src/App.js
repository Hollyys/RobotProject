import React, { useState, useRef } from 'react';
import knu from './knu.png';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewURL, setPreviewURL] = useState(null);
  const fileInputRef = useRef();

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);

    // 이미지를 미리보기하기 위해 파일 URL 생성
    const reader = new FileReader();
    reader.onloadend = () => {
      setPreviewURL(reader.result);
    };
    reader.readAsDataURL(file);
  };

  const handleSubmit = () => {
    if (!selectedFile) {
      console.error('No file selected');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    fetch('http://localhost:9000/upload', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      console.log('Upload success:', data);
    })
    .catch(error => {
      console.error('Error uploading:', error);
    });
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', fontFamily: 'Arial, sans-serif', backgroundColor: '#f0f0f0' }}>
      <img src={knu} alt="KNU logo Image" style={{ width: '400px', marginTop: '100px', marginBottom: '50px' }} />
      <p style={{ fontSize: '35px' , fontWeight: 'bold'}}>모바일 로봇 프로그래밍 중간과제</p>
      <p style={{ fontSize: '20px' }}>생성하고 싶은 이미지를 전송하세요</p>
      <input type="file" ref={fileInputRef} onChange={handleFileChange} style={{ marginBottom: '10px' }} />
      {previewURL && <img src={previewURL} alt="Preview" style={{ maxWidth: '100%', maxHeight: '300px', marginTop: '10px' }} />}
      <button onClick={handleSubmit} style={{ marginTop: '10px' , marginBottom: '50px'}}>Upload</button>
      <p style={{ fontSize: '15px', marginTop: '5px' , marginBottom: '5px'}}>컴퓨터학부 신성한</p>
      <p style={{ fontSize: '15px', marginTop: '5px' , marginBottom: '5px'}}>2017110157</p>
      <a href="https://github.com/Hollyys/RobotProject.git" style={{ fontSize: '15px', marginTop: '5px', marginBottom: '50px' }}>git repository</a>
    </div>
  );
}

export default App;
