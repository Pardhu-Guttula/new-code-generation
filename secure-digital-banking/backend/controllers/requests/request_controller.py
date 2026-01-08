from flask import Blueprint, request, jsonify
from backend.repositories.requests.request_repository import RequestRepository
from backend.services.requests.request_service import RequestService

request_controller = Blueprint('request_controller', __name__)
request_repository = RequestRepository()
request_service = RequestService(request_repository)

@request_controller.route('/requests', methods=['POST'])
def create_request():
    json_data = request.json
    user_id = json_data.get('user_id')
    type = json_data.get('type')
    details = json_data.get('details')
    status = json_data.get('status')

    request_entry = request_service.create_request(user_id, type, details, status)
    return jsonify(request_entry.dict()), 201

@request_controller.route('/requests/<int:request_id>', methods=['GET'])
def get_request(request_id: int):
    request_entry = request_service.get_request(request_id)
    return jsonify(request_entry.dict()), 200

@request_controller.route('/requests/user/<int:user_id>', methods=['GET'])
def get_user_requests(user_id: int):
    requests = request_service.get_user_requests(user_id)
    return jsonify([request_entry.dict() for request_entry in requests]), 200

@request_controller.route('/requests/<int:request_id>', methods=['PUT'])
def update_request(request_id: int):
    json_data = request.json
    request_entry = request_service.get_request(request_id)
    
    if not request_entry:
        return jsonify({'message': 'Request not found'}), 404
    
    request_data = json_data.dict()
    updated_request = request_service.update_request(request_data)
    return jsonify(updated_request.dict()), 200

@request_controller.route('/requests/<int:request_id>', methods=['DELETE'])
def delete_request(request_id: int):
    request_service.delete_request(request_id)
    return jsonify({'message': 'Request deleted successfully'}), 200