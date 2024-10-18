from app.config import Config

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@db_container:5432/database_name'
    MINIO_URL = 'TBD'
    MINIO_ACCESS_KEY = 'TBD'
    MINIO_SECRET_KEY = 'TBD'
    SECRET_KEY = 'TBD'
