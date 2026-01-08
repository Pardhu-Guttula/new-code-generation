from backend.repositories.cart.cart_repository import CartRepository
from backend.models.cart.cart import Cart, CartItem

class CartService:
    def __init__(self, cart_repository: CartRepository):
        self.cart_repository = cart_repository

    def get_cart(self, user_id: int) -> Cart:
        return self.cart_repository.get_cart_by_user_id(user_id)

    def add_product_to_cart(self, user_id: int, product_id: int, quantity: int) -> Cart:
        cart = self.cart_repository.get_cart_by_user_id(user_id)
        if not cart:
            cart = Cart(user_id=user_id, items=[], created_at=datetime.now(), updated_at=datetime.now())
        item = next((item for item in cart.items if item.product_id == product_id), None)
        if item:
            item.quantity += quantity
        else:
            cart.items.append(CartItem(product_id=product_id, quantity=quantity))
        cart.updated_at = datetime.now()
        return self.cart_repository.create_cart(cart)
    
    def remove_product_from_cart(self, user_id: int, product_id: int) -> Cart:
        cart = self.cart_repository.get_cart_by_user_id(user_id)
        if not cart:
            raise Exception('Cart not found')
        cart.items = [item for item in cart.items if item.product_id != product_id]
        cart.updated_at = datetime.now()
        return self.cart_repository.update_cart(cart)

    def clear_cart(self, user_id: int) -> None:
        self.cart_repository.delete_cart(user_id)