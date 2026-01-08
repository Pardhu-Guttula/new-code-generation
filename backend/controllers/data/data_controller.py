from flask import Blueprint, request, jsonify
from backend.services.encryption_service import EncryptionService
from backend.repositories.encrypted_data_repository import EncryptedDataRepository

data_controller = Blueprint('data_controller', __name__)

# Load or generate the encryption key securely
encryption_key = os.getenv('ENCRYPTION_KEY') or EncryptionService.generate_key()
encryption_service = EncryptionService(encryption_key)
encrypted_data_repository = EncryptedDataRepository(encryption_service)

@data_controller.route('/encrypt', methods=['POST'])
def encrypt_data():
    data = request.data
    encrypted_data = encrypted_data_repository.save(data)
    return jsonify({'encrypted_data': encrypted_data.decode()}), 200

@data_controller.route('/decrypt', methods=['POST'])
def decrypt_data():
    encrypted_data = request.data
    decrypted_data = encrypted_data_repository.retrieve(encrypted_data)
    return jsonify({'decrypted_data': decrypted_data.decode()}), 200