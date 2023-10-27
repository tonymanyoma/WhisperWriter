from flask import request, jsonify
from decouple import config
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        expected_token = config('AUTHORIZATION_TOKEN')
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Error token not found'}), 403

        if token != expected_token:
            return jsonify({'message': 'Error invalid token'}), 403

        return f(*args, **kwargs)

    return decorated