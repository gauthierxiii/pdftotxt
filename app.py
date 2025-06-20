# app.py
from flask import Flask, request, jsonify
import fitz  # PyMuPDF

app = Flask(__name__)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    file = request.files['file']
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    text = "\n".join(page.get_text() for page in pdf)
    return jsonify({"text": text})

if __name__ == '__main__':
    app.run()