import logging
from typing import Optional, List
from backend.repositories.products.category_repository import CategoryRepository
from backend.models.products.category import Category

logger = logging.getLogger(__name__)

class CategoryService:
    def __init__(self, category_repo: CategoryRepository) -> None:
        self._category_repo = category_repo

    def create_category(self, name: str, description: str, parent_id: Optional[int]) -> Category:
        if not name or not description:
            raise ValueError("Name and description cannot be empty")
        if self._category_repo.get_category_by_name(name):
            raise ValueError("Category name must be unique")
        logger.info("Creating new category with name='%s'", name)
        return self._category_repo.create_category(name, description, parent_id)

    def get_all_categories(self) -> List<Category]:
        logger.info("Service layer fetching all categories")
        return self._category_repo.get_all_categories()