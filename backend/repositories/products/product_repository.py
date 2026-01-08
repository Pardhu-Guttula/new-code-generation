from backend.models.products.product import Product
from typing import List, Optional

class ProductRepository:
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        pass  # Implement database retrieval logic here

    def get_product_by_name(self, name: str) -> Optional[Product]:
        pass  # Implement database retrieval logic here

    def create_product(self, product: Product) -> Product:
        pass  # Implement database creation logic here

    def update_product(self, product: Product) -> Product:
        pass  # Implement database update logic here

    def delete_product(self, product_id: int) -> None:
        pass  # Implement database deletion logic here

    def list_products(self) -> List[Product]:
        pass  # Implement database list retrieval logic here

    def search_products(self, query: str, page: int, page_size: int) -> List[Product]:
        pass  # Implement search logic here