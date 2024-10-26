from app.config import Config
import os
from dotenv import load_dotenv

load_dotenv()

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@postgres:5432/{os.getenv("POSTGRES_DB")}'
    #SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:autograde123@localhost:5432/autograde'