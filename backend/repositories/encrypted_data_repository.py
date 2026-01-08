from typing import Optional
from backend.services.encryption_service import EncryptionService

class EncryptedDataRepository:
    def __init__(self, encryption_service: EncryptionService):
        self.encryption_service = encryption_service

    def save(self, data: bytes) -> bytes:
        encrypted_data = self.encryption_service.encrypt(data)
        # Save encrypted_data to the database
        return encrypted_data

    def retrieve(self, encrypted_data: bytes) -> bytes:
        decrypted_data = self.encryption_service.decrypt(encrypted_data)
        return decrypted_data