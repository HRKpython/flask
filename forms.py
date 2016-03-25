from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, \
     SelectField, StringField, PasswordField, BooleanField, SubmitField
from wtforms_components import DateTimeField, DateRange
from wtforms.validators import DataRequired, EqualTo, Length, Email, Regexp

class LoginForm(Form):
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField ('Log In')

class RegisterForm(Form):
    name = StringField('Username', 
                       validators=[DataRequired(), Length(min=3, max=25), 
                                   Regexp('^[A-Za-z0-9_]{3,}$', message = 'Usernames consist of numbers, letters, and underscores.')]
                       )
# Email() has been added for Error Handeling 
    email = StringField('Email',
                       validators=[DataRequired(), Email(), Length(min=6, max=80)]
                       )
    password = PasswordField('Password',
                             validators = [DataRequired(), Length(min=6, max=40)]
                             )
    confirm = PasswordField('Repeat Password',
                             validators = [DataRequired(),
                                           EqualTo('password', message = 'Passwords must match')])