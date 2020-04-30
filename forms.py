from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import email_validator

class RegistrationForm(FlaskForm):
    username=StringField('Username',
    validators=[DataRequired(),Length(min=2,max=20)])
    email = EmailField('Email',
                        validators=[DataRequired(), Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',
    validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = EmailField('Email',
                        validators=[DataRequired(), Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit = SubmitField('Login')