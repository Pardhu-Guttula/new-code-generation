from cryptography.fernet import Fernet
import os

class EncryptionService:
    def __init__(self, key: str):
        self.cipher_suite = Fernet(key)

    def encrypt(self, data: bytes) -> bytes:
        return self.cipher_suite.encrypt(data)

    def decrypt(self, encrypted_data: bytes) -> bytes:
        return self.cipher_suite.decrypt(encrypted_data)

    @staticmethod
    def generate_key() -> str:
        key = Fernet.generate_key()
        return key.decode()