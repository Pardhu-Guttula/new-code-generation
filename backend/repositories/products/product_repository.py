import sqlite3
from datetime import datetime
from typing import Optional
from backend.models.products.product import Product
import logging

logger = logging.getLogger(__name__)

class ProductRepository:
    def __init__(self, db_path: str) -> None:
        self._db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self._db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        return conn

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        logger.info("Fetching product by id='%s'", product_id)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, description, price, category_id, is_deleted, created_at, updated_at FROM products WHERE id=?",
                (product_id,),
            )
            row = cursor.fetchone()
            return Product(*row) if row else None

    def update_product(self, product_id: int, name: str, description: str, price: float) -> None:
        logger.info("Updating product id='%s'", product_id)
        with self._get_connection() as conn:
            conn.execute(
                "UPDATE products SET name=?, description=?, price=?, updated_at=? WHERE id=?",
                (name, description, price, datetime.now(), product_id),
            )