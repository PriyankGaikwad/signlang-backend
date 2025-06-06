from flask import Blueprint, jsonify, request

bp = Blueprint('sign_routes', __name__)

@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'SignLang Flask backend is running ✅'}), 200

@bp.route('/predict-sign', methods=['POST'])
def predict_sign():
    # Placeholder for now
    return jsonify({'prediction': 'Hello'}), 200
