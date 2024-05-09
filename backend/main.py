import os, time
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from gcode_generator import generator
from flask_cors import CORS
import threading

sema = threading.Semaphore(1)


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
GCODE_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/gcode/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename): # filename을 보고 지원하는 media type인지 판별
    filename = filename.lower()
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GCODE_FOLDER'] = GCODE_FOLDER

CORS(app)

# 업로드 HTML 렌더링
@app.route('/')
def render_file():
    return 'Mobile Robot Programming Mid Project'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
        
    file = request.files['file']
    filename = file.filename
    
    if filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if not allowed_file(filename):
        return jsonify({'message': 'unsupported media type'}), 415
    
    sta = time.time() # 시간 측정
    sema.acquire() # 세마포어 획득

    file.save(os.path.join(app.config['UPLOAD_FOLDER'] + filename))
    img_dir = UPLOAD_FOLDER + filename
    
    g_code = generator(img_dir)
    gcode_filepath = os.path.join(app.config['GCODE_FOLDER'])+"gcode.txt"
    with open(gcode_filepath, 'w') as gcode_file:
        gcode_file.write(g_code)

    print(filename, ": g_code generated.")
    sema.release() # 세마포어 릴리즈
        
    return jsonify({'message': 'gcode generated successfully', 'path': img_dir}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)