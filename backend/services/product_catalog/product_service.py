from backend.repositories.products.product_repository import ProductRepository
from backend.models.products.product import Product

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def add_product(self, product_data: Product) -> Product:
        new_product = Product(**product_data.dict(), created_at=datetime.now(), updated_at=datetime.now())
        return self.product_repository.create_product(new_product)

    def update_product(self, product_id: int, product_data: Product) -> Product:
        existing_product = self.product_repository.get_product_by_id(product_id)
        if not existing_product:
            raise Exception('Product not found')
        updated_data = product_data.dict(exclude_unset=True)
        if 'description' in updated_data and not updated_data['description']:
            updated_data.pop('description')
        for key, value in updated_data.items():
            setattr(existing_product, key, value)
        existing_product.updated_at = datetime.now()
        return self.product_repository.update_product(existing_product)

    def get_product(self, product_id: int) -> Product:
        return self.product_repository.get_product_by_id(product_id)

    def delete_product(self, product_id: int) -> None:
        self.product_repository.delete_product(product_id)

    def list_products(self) -> List[Product]:
        return self.product_repository.list_products()

    def search_products(self, query: str, page: int, page_size: int) -> List[Product]:
        return self.product_repository.search_products(query, page, page_size)