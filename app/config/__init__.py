class Config:
    """Base configuration."""
    SECRET_KEY = 'TBD'  # Replace with env var in production
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False