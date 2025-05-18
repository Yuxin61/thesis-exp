from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware

from .database import SessionLocal, engine, Base
from .users import user_routers
from .products import product_routers
from .orders import order_routers

import os, dotenv

dotenv.load_dotenv('.env')


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ProShop API",
    description="This is the API for ProShop e-Commerce",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    DBSessionMiddleware,
    db_url=os.environ.get("DB_URI")
)

# app.add_middleware(HTTPSRedirectMiddleware)

app.include_router(user_routers.router)
app.include_router(product_routers.router)
app.include_router(order_routers.router)
# app.include_router(review_routers.router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}
