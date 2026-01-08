import logging
from backend.repositories.products.product_repository import ProductRepository
from backend.models.products.product import Product

logger = logging.getLogger(__name__)

class ProductDeletionService:
    def __init__(self, product_repo: ProductRepository) -> None:
        self._product_repo = product_repo

    def delete_product(self, product_id: int) -> None:
        product = self._product_repo.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        if product.is_deleted:
            raise ValueError("Product is already deleted")
        logger.info("Deleting product id='%s'", product_id)
        self._product_repo.delete_product(product_id)