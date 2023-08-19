from app import app

from user.view import user

app.register_blueprint(user, url_prefix="/user")

if __name__ == '__main__':
    app.run()
