import React, { useState } from 'react';

function App() {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageChange = (event) => {
    setSelectedImage(URL.createObjectURL(event.target.files[0]));
  };

  const handleUpload = () => {
    const formData = new FormData();
    formData.append('image', selectedImage);

    fetch('http://localhost:5000/upload', {
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
    <div>
      <input type="file" onChange={handleImageChange} />
      {selectedImage && (
        <div>
          <img src={selectedImage} alt="Uploaded" style={{ width: '300px', marginTop: '20px' }} />
          <button onClick={handleUpload}>Upload</button>
        </div>
      )}
    </div>
  );
}

export default App;