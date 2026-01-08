import sqlite3
from datetime import datetime
from typing import List, Optional
from backend.models.products.category import Category
import logging

logger = logging.getLogger(__name__)

class CategoryRepository:
    def __init__(self, db_path: str) -> None:
        self._db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self._db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        return conn

    def create_category(self, name: str, description: str, parent_id: Optional[int]) -> Category:
        logger.info("Creating category with name='%s'", name)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            created_at = datetime.now()
            cursor.execute(
                "INSERT INTO categories (name, description, parent_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                (name, description, parent_id, created_at, created_at),
            )
            category_id = cursor.lastrowid
        return Category(id=category_id, name=name, description=description, parent_id=parent_id, created_at=created_at, updated_at=created_at)

    def get_category_by_name(self, name: str) -> Optional<Category]:
        logger.info("Fetching category by name='%s'", name)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, description, parent_id, created_at, updated_at FROM categories WHERE name=?",
                (name,),
            )
            row = cursor.fetchone()
            return Category(*row) if row else None

    def get_all_categories(self) -> List[Category]:
        logger.info("Fetching all categories")
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, description, parent_id, created_at, updated_at FROM categories"
            )
            rows = cursor.fetchall()
            return [Category(*row) for row in rows]