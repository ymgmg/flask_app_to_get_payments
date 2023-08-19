from app import app, db
from user.model import *

with app.app_context():
    db.create_all()
