from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()

# from supabase import create_client, Client

# url: str = os.getenv("SUPABASE_URL")
# key: str = os.getenv("SUPABASE_KEY")

# supabase_instance: Client = create_client(url, key)


# URL_OBJECT = URL.create(
#     drivername="postgresql+psycopg2",
#     username=os.getenv("DB_USERNAME"),
#     password=os.getenv("DB_PASSWORD"),
#     host=os.getenv("DB_HOST"),
#     port=os.getenv("DB_PORT"),
#     database=os.getenv("DB_NAME")
# )

URL_OBJECT = os.getenv("DB_URI")

engine = create_engine(URL_OBJECT)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
