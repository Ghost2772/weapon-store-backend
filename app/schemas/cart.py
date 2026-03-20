from decimal import Decimal
from pydantic import BaseModel


class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = 1


class CartItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str
    price: Decimal
    quantity: int
    total_price: Decimal

    class Config:
        from_attributes = True


class CartResponse(BaseModel):
    id: int
    user_id: int
    items: list[CartItemResponse]
    total_amount: Decimal