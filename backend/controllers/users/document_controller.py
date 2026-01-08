from flask import Blueprint, request, jsonify, send_file
from backend.services.documents.document_service import DocumentService
from backend.repositories.documents.document_repository import DocumentRepository

document_controller = Blueprint('document_controller', __name__)
document_repository = DocumentRepository()
encryption_key = b'your-encryption-key'  # Store this securely, e.g., in environment variables
document_service = DocumentService(document_repository, encryption_key)

@document_controller.route('/documents', methods=['POST'])
def upload_document():
    user_id = request.form.get('user_id')
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']

    if not user_id or file.filename == '':
        return jsonify({'message': 'User ID and file are required'}), 400

    document = document_service.save_document(int(user_id), file.filename, file.read())
    return jsonify(document.dict()), 201

@document_controller.route('/documents', methods=['GET'])
def get_documents():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400

    documents = document_service.get_user_documents(int(user_id))
    return jsonify([document.dict() for document in documents]), 200

@document_controller.route('/documents/<int:document_id>', methods=['GET'])
def download_document(document_id):
    document = document_service.get_document(document_id)
    if not document:
        return jsonify({'message': 'Document not found'}), 404

    decrypted_file_path = document_service.decrypt_file(document.file_path)
    return send_file(decrypted_file_path, as_attachment=True)