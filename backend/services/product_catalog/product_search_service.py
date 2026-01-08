import logging
from typing import List, Optional
from backend.repositories.products.product_repository import ProductRepository
from backend.models.products.product import Product

logger = logging.getLogger(__name__)

class ProductSearchService:
    def __init__(self, product_repo: ProductRepository) -> None:
        self._product_repo = product_repo

    def search_products(self, query: str, category_id: Optional[int] = None, page: int = 1, per_page: int = 10) -> List[Product]:
        logger.info("Service layer search for products with query='%s', category_id=%s, page=%d, per_page=%d", query, category_id, page, per_page)
        return self._product_repo.search_products(query, category_id, page, per_page)