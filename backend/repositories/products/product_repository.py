import sqlite3
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

    def search_products(self, query: str, category_id: Optional[int] = None, page: int = 1, per_page: int = 10) -> List[Product]:
        logger.info("Searching products with query='%s', category_id=%s", query, category_id)
        offset = (page - 1) * per_page
        with self._get_connection() as conn:
            cursor = conn.cursor()
            sql_query = """
                SELECT id, name, description, price, category_id, is_deleted, created_at, updated_at
                FROM products
                WHERE (name LIKE ? OR description LIKE ?)
                AND is_deleted = 0
            """
            params = [f"%{query}%", f"%{query}%"]
            if category_id:
                sql_query += " AND category_id = ?"
                params.append(category_id)
            sql_query += " LIMIT ? OFFSET ?"
            params.extend([per_page, offset])
            cursor.execute(sql_query, params)
            rows = cursor.fetchall()
            return [Product(*row) for row in rows]