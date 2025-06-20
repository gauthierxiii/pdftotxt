from flask import Flask, request, jsonify
import pdfplumber

app = Flask(__name__)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    file = request.files['file']
    with pdfplumber.open(file) as pdf:
        text = '\n'.join([page.extract_text() or '' for page in pdf.pages])
    return jsonify({'text': text.strip()})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
