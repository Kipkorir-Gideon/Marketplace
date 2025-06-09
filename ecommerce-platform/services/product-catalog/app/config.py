from pydantic import BaseSettings, PostgresDsn
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn = "postgresql+asyncpg://ngetich:.ecommerce@localhost:5432/product_catalog"
    MONGO_URL: str = "mongodb://mongodb:27017/producr_db"
    ELASTICSEARCH_URL: str = "http://elasticsearch:9200"
    JWT_SECRET: str = "your-secret-key"
    
    class Config:
        env_file = ".env"
        
settings = Settings()