from flask import Flask
from app.config.development import DevelopmentConfig  # Import configuration
from app.extensions import db, minio#, kcclient  # Import extensions
#from app.blueprints.auth import auth_bp  # Import blueprints
#from app.blueprints.product import product_bp

def create_app(config_class=DevelopmentConfig):
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(config_class)  # Load configuration

    # Initialize Flask extensions
    db.init_app(app)
    minio.init_app(app)
    #kcclient.pat()

    # Register blueprints
    #app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/')
    def index():
        return {"message": "Welcome to the Autograde.dev API!"}, 200

    return app