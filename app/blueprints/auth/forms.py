from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import random
from jinja2.utils import markupsafe
from ...models import User

class LoginForm(FlaskForm):
    email =StringField("Email Address", validators=[DataRequired(),Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name=StringField('First Name', validators=[DataRequired()]) 
    last_name= StringField('Last Name', validators=[DataRequired()])
    email=StringField('email', validators=[DataRequired(),Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',
            validators=[DataRequired(), EqualTo('password', message='Password Must Match')])
    submit= SubmitField('Register') 

    img = markupsafe.Markup(f'<img src="https://avatars.dicebear.com/api/initials/{first_name}.svg" height="75px">')
    icon = RadioField('Avatar', validators=[DataRequired()],
        choices=[(img)])
    
    
    def validate_email(form,field):
        same_email_user = User.query.filter_by(email = field.data).first()
        if same_email_user:
            raise ValidationError('Email is Already in Use')

class EditProfileForm(FlaskForm):
    first_name=StringField('First Name', validators=[DataRequired()]) 
    last_name= StringField('Last Name', validators=[DataRequired()])
    email=StringField('email', validators=[DataRequired(),Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',
            validators=[DataRequired(), EqualTo('password', message='Password Must Match')])
    submit= SubmitField('Register') 

    img = markupsafe.Markup(f'<img src="https://avatars.dicebear.com/api/initials/{first_name}.svg" height="75px">')
    
    icon = RadioField('Avatar', validators=[DataRequired()],
        choices=[(9000, "Don't Change"),(img)])

class BiteForm(FlaskForm):
    location =StringField('Enter your city', validators=[DataRequired()])
    submit = SubmitField('Submit')