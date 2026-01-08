from pydantic import BaseModel, Field

class DashboardOverview(BaseModel):
    user_id: int
    total_balance: float
    upcoming_bills: int
    recent_transactions: int

    class Config:
        orm_mode = True