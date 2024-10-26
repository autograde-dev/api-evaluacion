from flask_sqlalchemy import SQLAlchemy
from keycloak import keycloak_openid
import os

db = SQLAlchemy()
kcoi = keycloak_openid
