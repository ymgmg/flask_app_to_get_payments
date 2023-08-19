from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Configuration
# from user.model import User

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "user.login"


@app.route("/")
def index():
    return render_template("index.html")
