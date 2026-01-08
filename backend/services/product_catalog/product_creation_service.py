import logging
from backend.repositories.products.product_repository import ProductRepository
from backend.models.products.product import Product

logger = logging.getLogger(__name__)

class ProductCreationService:
    def __init__(self, product_repo: ProductRepository) -> None:
        self._product_repo = product_repo

    def create_product(self, name: str, description: str, price: float, category_id: int) -> Product:
        if not name or not description:
            raise ValueError("Name and description cannot be empty")
        if self._product_repo.get_product_by_name(name):
            raise ValueError("Product name must be unique")
        if price <= 0:
            raise ValueError("Product price must be a positive number")
        logger.info("Creating new product with name='%s'", name)
        return self._product_repo.create_product(name, description, price, category_id)