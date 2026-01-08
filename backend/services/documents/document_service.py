import os
import uuid
from typing import List
from cryptography.fernet import Fernet
from backend.models.documents import Document
from backend.repositories.documents.document_repository import DocumentRepository

class DocumentService:
    def __init__(self, document_repository: DocumentRepository, encryption_key: str):
        self.document_repository = document_repository
        self.encryption_key = encryption_key
        self.cipher_suite = Fernet(self.encryption_key)

    def encrypt_file(self, file_path: str) -> str:
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.cipher_suite.encrypt(file_data)
        encrypted_file_path = f"{file_path}.enc"
        with open(encrypted_file_path, 'wb') as file:
            file.write(encrypted_data)
        os.remove(file_path)
        return encrypted_file_path

    def decrypt_file(self, encrypted_file_path: str) -> str:
        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        original_file_path = encrypted_file_path.replace('.enc', '')
        with open(original_file_path, 'wb') as file:
            file.write(decrypted_data)
        return original_file_path

    def save_document(self, user_id: int, file_name: str, file_data: bytes) -> Document:
        file_path = os.path.join('uploads', f"{uuid.uuid4()}_{file_name}")
        with open(file_path, 'wb') as file:
            file.write(file_data)
        encrypted_file_path = self.encrypt_file(file_path)
        document = Document(user_id=user_id, file_name=file_name, file_path=encrypted_file_path)
        return self.document_repository.create(document)

    def get_user_documents(self, user_id: int) -> List<Document]:
        return self.document_repository.find_by_user_id(user_id)

    def get_document(self, document_id: int) -> Document:
        return self.document_repository.find_by_id(document_id)