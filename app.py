from flask import Flask, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
from model import process_image, generate_palmistry_reading
from pdf_parser import extract_info_from_pdf

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PDF_FOLDER = 'pdfs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return send_from_directory('..', 'frontend/index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        image_data = process_image(file_path)
        reading = generate_palmistry_reading(image_data)
        info = extract_info_from_pdf(PDF_FOLDER)
        return jsonify({'reading': reading, 'info': info}), 200

if __name__ == '__main__':
    app.run(debug=True)
