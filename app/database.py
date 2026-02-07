from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv 

load_dotenv()

DB_HOST = os.getenv('DB_HOST','localhost')
DB_PORT = os.getenv('DB_PORT','5433')
DB_NAME = os.getenv('DB_NAME','FishingDB')
DB_USER = os.getnev('DB_USER','postgers')
DB_PASSWORD = os.getenv('DV_PASSWORD','77777')


DATABSE_URL = f"postgersql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABSE_URL, echo=True)
#echo=True - Включает логирование SQL-запросов
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session