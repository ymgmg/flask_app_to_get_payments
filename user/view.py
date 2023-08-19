from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from app import db, login_manager
from .form import LoginForm, RegistrationForm
from .model import User

user = Blueprint("user", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@user.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    return render_template("user/login.html", form=LoginForm())


@user.route("/login-process", methods=["POST"])
def login_process():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        print("USERRRR", user)
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            flash("SUCCESS")
            return redirect(url_for("index"))
        flash("mission failed")
        return redirect(url_for("user.login"))
    flash("sucks")
    return redirect(url_for("user.login"))


@user.route("/logout")
def logout():
    logout_user()
    flash("you logged out")
    return redirect(url_for("index"))


@user.route("/registration")
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    return render_template("user/registration.html", form=RegistrationForm())


@user.route("/registration-process", methods=["POST"])
def registration_process():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data, role="user")
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        print("its ok")
        flash("SUCCESS")
        return redirect(url_for("index"))
    else:
        flash("mission failed")
        return redirect(url_for("user.registration"))
