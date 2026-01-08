from typing import List
from backend.models.documents.document import Document
from backend.repositories.documents.document_repository import DocumentRepository

class DocumentService:
    def __init__(self, document_repository: DocumentRepository):
        self.document_repository = document_repository

    def create_document(self, user_id: int, title: str, content: str) -> Document:
        document = Document(user_id=user_id, title=title, content=content)
        return self.document_repository.create(document)

    def get_document(self, document_id: int) -> Document:
        return self.document_repository.find_by_id(document_id)

    def get_user_documents(self, user_id: int) -> List<Document]:
        return self.document_repository.find_by_user_id(user_id)

    def update_document(self, document: Document) -> Document:
        return self.document_repository.update(document)

    def delete_document(self, document_id: int) -> None:
        self.document_repository.delete(document_id)