from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired , Email ,Length , EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email' , validators=[DataRequired() , Email() , Length(min=12 , max=50)])
    password = PasswordField('Password' , validators=[DataRequired() , Length(min = 8 , max=50)])
    submit = SubmitField('Login')
    
class RegisterForm(FlaskForm):
    email = StringField('Email' , validators=[DataRequired() , Email() , Length(min=12 , max=50)])
    password = PasswordField('Password' , validators=[DataRequired() , Length(min = 8 , max=50)])
    confirm = PasswordField('Confirm' , validators=[DataRequired() , Length(min = 8 , max = 50) , EqualTo("password" , message="Password not match") ])
    name = StringField('Name' , validators=[DataRequired() , Length(min = 3 , max = 50)])
    submit = SubmitField('Register')
    