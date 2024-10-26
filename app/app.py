from flask import Flask
from app.config.development import DevelopmentConfig  # Import configuration
from app.extensions import db
from app.controllers.exams_controller import exams_bp  # Import blueprints
from app.controllers.questions_controller import questions_bp

def create_app(config_class=DevelopmentConfig):
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(config_class)  # Load configuration

    # Initialize Flask extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(exams_bp, url_prefix='/exams')
    app.register_blueprint(questions_bp, url_prefix='/questions')

    @app.route('/')
    def index():
        return {"message": "Welcome to the Autograde.dev API!"}, 200

    return app