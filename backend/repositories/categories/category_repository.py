from backend.models.categories.category import Category
from typing import List, Optional

class CategoryRepository:
    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        pass  # Implement database retrieval logic here

    def create_category(self, category: Category) -> Category:
        pass  # Implement database creation logic here

    def update_category(self, category: Category) -> Category:
        pass  # Implement database update logic here

    def delete_category(self, category_id: int) -> None:
        pass  # Implement database deletion logic here

    def list_categories(self) -> List[Category]:
        pass  # Implement database list retrieval logic here