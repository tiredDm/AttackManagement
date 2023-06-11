from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import (
    InputRequired,
    DataRequired,
    NumberRange,
    Length,
    Email,
    EqualTo,
    ValidationError,
    Regexp
)
import re

from .models import User, Attack

class AttackRegisterForm(FlaskForm):
    name = TextAreaField(
        "name", validators=[InputRequired(), Length(min=1, max=100)]
    )
    type = TextAreaField(
        "type", validators=[InputRequired(), Length(min=1, max=100)]
    )
    damage = TextAreaField(
        "damage", validators=[InputRequired(), Length(min=1, max=100)]
    )
    submit = SubmitField("Submit Attack")
    
class AttackUpdate(FlaskForm):
    name = TextAreaField("name", validators=[InputRequired(), Length(min=1, max=100)])
    def validate_password(self, name):
        if(name.data):
            raise ValidationError("Is not a saved attack")
    type = TextAreaField(
        "type", validators=[InputRequired(), Length(min=1, max=100)]
    )
    damage = TextAreaField(
        "damage", validators=[InputRequired(), Length(min=1, max=100)]
    )
    submit = SubmitField("Update Attack")
 #   attack = Attack.objects(name = name.data, type = type.damage, damage = damage.type).first()

class AttackSubmit(FlaskForm):


    damage = StringField( "damage", validators=[InputRequired(), Length(min=1, max=100), Regexp("[0-9]*d[0-9]+")])
    isCrit = TextAreaField(
        "isCrit", validators=[Length(min=0, max=100)]
    )
    submit = SubmitField("Submit Attack")
    
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min = 12, max = 120)])
    def validate_password(self, password):
        if(password.data.islower()):
            raise ValidationError("Does not contain an Uppercase letter (A-Z)")
        if(password.data.isupper()):
            raise ValidationError("Does not contain a Lowercase letter (a-z)")
        if(re.search(r'\d', password.data) == False):
            raise ValidationError("Does not contain a number (0-9)")
        if (any(c in "!@#$%^&*()_+=<>-" for c in password.data) == False):
            raise ValidationError("Does not contain a special character(!-*)")
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")
        


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")


class UpdateUsernameForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    submit = SubmitField("Update Username")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.objects(username=username.data).first()
            if user is not None:
                raise ValidationError("That username is already taken")
