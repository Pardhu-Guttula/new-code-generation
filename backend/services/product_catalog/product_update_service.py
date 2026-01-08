import logging
from backend.repositories.products.product_repository import ProductRepository
from backend.models.products.product import Product

logger = logging.getLogger(__name__)

class ProductUpdateService:
    def __init__(self, product_repo: ProductRepository) -> None:
        self._product_repo = product_repo

    def update_product(self, product_id: int, name: str, description: str, price: float) -> Product:
        if not name or not description:
            raise ValueError("Name and description cannot be empty")
        if price <= 0:
            raise ValueError("Product price must be a positive number")
        if not self._product_repo.get_product_by_id(product_id):
            raise ValueError("Product not found")
        logger.info("Updating product id='%s'", product_id)
        self._product_repo.update_product(product_id, name, description, price)
        return self._product_repo.get_product_by_id(product_id)