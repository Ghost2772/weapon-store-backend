from decimal import Decimal
from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    stock: int
    category_id: int
    is_active: bool = True


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: Decimal
    stock: int
    is_active: bool
    category_id: int

    class Config:
        from_attributes = True