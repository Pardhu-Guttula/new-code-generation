import logging
from typing import List
from backend.repositories.cart.shopping_cart_repository import ShoppingCartRepository
from backend.models.cart.shopping_cart import ShoppingCart, CartItem

logger = logging.getLogger(__name__)

class CartService:
    def __init__(self, cart_repo: ShoppingCartRepository) -> None:
        self._cart_repo = cart_repo

    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> ShoppingCart:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        logger.info("Service layer adding product '%s' to cart for user '%s'", product_id, user_id)
        return self._cart_repo.add_to_cart(user_id, product_id, quantity)

    def remove_from_cart(self, user_id: int, product_id: int) -> ShoppingCart:
        logger.info("Service layer removing product '%s' from cart for user '%s'", product_id, user_id)
        return self._cart_repo.remove_from_cart(user_id, product_id)
    
    def update_cart_item(self, user_id: int, product_id: int, quantity: int) -> ShoppingCart:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        logger.info("Service layer updating product '%s' quantity to '%s' for user '%s'", product_id, quantity, user_id)
        return self._cart_repo.update_cart_item(user_id, product_id, quantity)