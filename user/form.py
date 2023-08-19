from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from .model import User

for_html = {"class": "form-control"}


class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email()], render_kw=for_html)
    password = PasswordField(
        "Password", validators=[DataRequired()], render_kw=for_html)
    submit = SubmitField("Log in", render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_repeat = PasswordField(
        "Repeat password", validators=[DataRequired(), EqualTo("password")])

    def validate_email(self, email):
        user_count = User.query.filter_by(email=email.data).count()
        if user_count > 0:
            raise ValidationError(
                f"Email {email.data} is already used by other user")
