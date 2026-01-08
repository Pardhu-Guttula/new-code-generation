import sqlite3
from datetime import datetime
from typing import List, Optional
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

    def create_product(self, name: str, description: str, price: float, category_id: int) -> Product:
        logger.info("Creating product with name='%s'", name)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            created_at = datetime.now()
            cursor.execute(
                "INSERT INTO products (name, description, price, category_id, is_deleted, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (name, description, price, category_id, False, created_at, created_at),
            )
            product_id = cursor.lastrowid
        return Product(id=product_id, name=name, description=description, price=price, category_id=category_id, is_deleted=False, created_at=created_at, updated_at=created_at)

    def get_product_by_name(self, name: str) -> Optional[Product]:
        logger.info("Fetching product by name='%s'", name)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, description, price, category_id, is_deleted, created_at, updated_at FROM products WHERE name=?",
                (name,),
            )
            row = cursor.fetchone()
            return Product(*row) if row else None