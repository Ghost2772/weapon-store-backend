from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import engine, Base
from app.models.user import User
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.order import Order
from app.models.order_item import OrderItem
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.catalog import router as catalog_router
from app.routers.cart import router as cart_router
from app.routers.orders import router as orders_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Weapon Store API",
    version="1.0",
    lifespan=lifespan
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(catalog_router)
app.include_router(cart_router)
app.include_router(orders_router)


@app.get("/")
def root():
    return {"message": "API работает"}