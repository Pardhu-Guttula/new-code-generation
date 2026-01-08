import sqlite3
from datetime import datetime
from typing import List
from backend.models.cart.shopping_cart import ShoppingCart, CartItem
import logging

logger = logging.getLogger(__name__)

class ShoppingCartRepository:
    def __init__(self, db_path: str) -> None:
        self._db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self._db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        return conn

    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> ShoppingCart:
        logger.info("Adding product '%s' to cart for user '%s'", product_id, user_id)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cart_items (user_id, product_id, quantity, created_at, updated_at) VALUES (?, ?, ?, ?, ?) "
                "ON CONFLICT(user_id, product_id) DO UPDATE SET quantity = quantity + ?, updated_at = ?",
                (user_id, product_id, quantity, datetime.now(), datetime.now(), quantity, datetime.now())
            )
            items = self.get_cart_items(user_id)
            return ShoppingCart(user_id=user_id, items=items, created_at=datetime.now(), updated_at=datetime.now())

    def get_cart_items(self, user_id: int) -> List[CartItem]:
        logger.info("Fetching cart items for user '%s'", user_id)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT product_id, quantity FROM cart_items WHERE user_id=?",
                (user_id,)
            )
            rows = cursor.fetchall()
            return [CartItem(*row) for row in rows]

    def remove_from_cart(self, user_id: int, product_id: int) -> ShoppingCart:
        logger.info("Removing product '%s' from cart for user '%s'", product_id, user_id)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM cart_items WHERE user_id=? AND product_id=?",
                (user_id, product_id)
            )
            items = self.get_cart_items(user_id)
            return ShoppingCart(user_id=user_id, items=items, created_at=datetime.now(), updated_at=datetime.now())

    def update_cart_item(self, user_id: int, product_id: int, quantity: int) -> ShoppingCart:
        logger.info("Updating product '%s' quantity to '%s' for user '%s'", product_id, quantity, user_id)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE cart_items SET quantity = ?, updated_at = ? WHERE user_id = ? AND product_id = ?",
                (quantity, datetime.now(), user_id, product_id)
            )
            items = self.get_cart_items(user_id)
            return ShoppingCart(user_id=user_id, items=items, created_at=datetime.now(), updated_at=datetime.now())