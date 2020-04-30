from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator
from flaskblog.models import User
from flask_login import current_user
class RegistrationForm(FlaskForm):
    username=StringField('Username',
    validators=[DataRequired(),Length(min=2,max=20)])
    email = EmailField('Email',
                        validators=[DataRequired(), Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',
    validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')

    #Validation of this form
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')
    #Validation of this form
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists')
class LoginForm(FlaskForm):
    email = EmailField('Email',
                        validators=[DataRequired(), Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username=StringField('Username',
    validators=[DataRequired(),Length(min=2,max=20)])
    email = EmailField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    #Validation of this form
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exists')
    #Validation of this form
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exists')