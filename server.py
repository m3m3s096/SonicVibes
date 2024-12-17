from flask import Flask, send_file, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Папка с аудиофайлами
AUDIO_FOLDER = 'audio_files'

if not os.path.exists(AUDIO_FOLDER):
    os.makedirs(AUDIO_FOLDER)

@app.route('/api/files', methods=['GET'])
def list_files():
    files = os.listdir(AUDIO_FOLDER)
    return jsonify(files)

@app.route('/api/play/<filename>', methods=['GET'])
def play_file(filename):
    return send_file(os.path.join(AUDIO_FOLDER, filename), as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
