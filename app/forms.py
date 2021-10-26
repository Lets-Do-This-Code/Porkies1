from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, PasswordField, BooleanField, RadioField
from wtforms.validators import DataRequired, EqualTo


class SigninForm(FlaskForm):
    email1 = StringField('Email', validators=[DataRequired()])
    paskey = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit1 = SubmitField('Sign In')

    
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()] )
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    alert = RadioField('Level of alert', choices=[('fair','Fair'),('poor','Poor'),('very_poor','Very poor'),('hazardous','Hazardous')],validators=[DataRequired()])
    message = RadioField('Message type', choices=[('sms','Phone/SMS'),('email','Email')],validators=[DataRequired()])
    submit = SubmitField('Register me')









