from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, slots=True)
class Category:
    id: int
    name: str
    description: str
    parent_id: Optional[int]
    created_at: datetime
    updated_at: datetime