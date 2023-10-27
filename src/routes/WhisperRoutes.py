from flask import Blueprint, jsonify, request
from utils.Whisper import WhisperProcess
from middleware.AuthorizationMiddleware import token_required 

main = Blueprint('movie_blueprint', __name__)


@main.route('/process_audio', methods=['POST'])
@token_required
def process_audio():
    try:
        audioRecord = request.files['audio']
        print(audioRecord)
        response = WhisperProcess.convert_audio(audioRecord)
        if response:
            return jsonify({'response': response}), 200
        else:
            return jsonify({'response': 'Error to generate text'}), 400
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
