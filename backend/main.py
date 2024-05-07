from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from gcode_generator import generator

app = Flask(__name__)

# 업로드 HTML 렌더링
@app.route('/')
def render_file():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image_file = request.files['image']
    # 이미지 처리 로직을 여기에 추가
    img_dir = '/uploads/'+secure_filename(image_file.filename)
    image_file.save(img_dir)
    g_code = generator(img_dir)
    # 이미지 처리 완료 후 응답
    print(g_code)
    print('message: Image uploaded successfully')
    return jsonify({'message': 'Image uploaded successfully'}), 200

if __name__ == "__main__":
    app.run(debug=True)