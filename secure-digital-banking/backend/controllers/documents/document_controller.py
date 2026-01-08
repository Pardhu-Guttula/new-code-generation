from flask import Blueprint, request, jsonify
from backend.repositories.documents.document_repository import DocumentRepository
from backend.services.documents.document_service import DocumentService

document_controller = Blueprint('document_controller', __name__)
document_repository = DocumentRepository()
document_service = DocumentService(document_repository)

@document_controller.route('/documents', methods=['POST'])
def create_document():
    json_data = request.json
    user_id = json_data.get('user_id')
    title = json_data.get('title')
    content = json_data.get('content')

    document = document_service.create_document(user_id, title, content)
    return jsonify(document.dict()), 201

@document_controller.route('/documents/<int:document_id>', methods=['GET'])
def get_document(document_id: int):
    document = document_service.get_document(document_id)
    return jsonify(document.dict()), 200

@document_controller.route('/documents/user/<int:user_id>', methods=['GET'])
def get_user_documents(user_id: int):
    documents = document_service.get_user_documents(user_id)
    return jsonify([document.dict() for document in documents]), 200

@document_controller.route('/documents/<int:document_id>', methods=['PUT'])
def update_document(document_id: int):
    json_data = request.json
    document = document_service.get_document(document_id)
    
    if not document:
        return jsonify({'message': 'Document not found'}), 404
    
    document_data = json_data.dict()
    updated_document = document_service.update_document(document_data)
    return jsonify(updated_document.dict()), 200

@document_controller.route('/documents/<int:document_id>', methods=['DELETE'])
def delete_document(document_id: int):
    document_service.delete_document(document_id)
    return jsonify({'message': 'Document deleted successfully'}), 200