from backend.repositories.products.product_repository import ProductRepository
from backend.repositories.categories.category_repository import CategoryRepository
from backend.models.products.product import Product
from backend.models.categories.category import Category

class ProductService:
    def __init__(self, product_repository: ProductRepository, category_repository: CategoryRepository):
        self.product_repository = product_repository
        self.category_repository = category_repository

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
    
    def add_category(self, category_data: Category) -> Category:
        new_category = Category(**category_data.dict(), created_at=datetime.now(), updated_at=datetime.now())
        return self.category_repository.create_category(new_category)
    
    def update_category(self, category_id: int, category_data: Category) -> Category:
        existing_category = self.category_repository.get_category_by_id(category_id)
        if not existing_category:
            raise Exception('Category not found')
        updated_data = category_data.dict(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(existing_category, key, value)
        existing_category.updated_at = datetime.now()
        return self.category_repository.update_category(existing_category)

    def get_category(self, category_id: int) -> Category:
        return self.category_repository.get_category_by_id(category_id)

    def delete_category(self, category_id: int) -> None:
        self.category_repository.delete_category(category_id)

    def list_categories(self) -> List[Category]:
        return self.category_repository.list_categories()