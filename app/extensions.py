from flask_sqlalchemy import SQLAlchemy
from flask_minio import Minio
from keycloak.extensions.flask import Client

db = SQLAlchemy()
minio = Minio()
kcclient = Client()