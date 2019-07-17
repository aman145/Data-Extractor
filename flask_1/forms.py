from flask_wtf import FlaskForm
from flask_wtf.file import FileField ,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_1.models import user

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')


class RegistrationForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired(),Length(min=2,max=20)]) 
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')
        
    def validate_username(self,username):
        
        User=user.query.filter_by(username=username.data).first()
        
        if User:
            raise ValidationError('Username is taken .Please try again.')
    
    def validate_email(self,email):
        
        User=user.query.filter_by(email=email.data).first()
        
        if User:
            raise ValidationError('Email is exists .Please try again.')
    
class UpdateAccountForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired(),Length(min=2,max=20)]) 
    email=StringField('Email',validators=[DataRequired(),Email()])
    picture =FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')
        
    def validate_username(self,username):
        if username.data != current_user.username:
            User=user.query.filter_by(username=username.data).first()
            
            if User:
                raise ValidationError('Username is taken .Please try again.')
        
    def validate_email(self,email):
        if email.data != current_user.email:
            User=user.query.filter_by(email=email.data).first()
            
            if User:
                raise ValidationError('Email is exists .Please try again.')



class DataForm1(FlaskForm):
    picture =FileField('Insert Image',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Insert')
    
class DataForm2(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(min=2,max=24)])
    age=IntegerField('Age',validators=[DataRequired()])
    lab_name=StringField('Lab',validators=[DataRequired(),Length(min=2,max=24)])
    parameter_name=StringField('Parameter')
    value_to_change=StringField('Value')
    submit=SubmitField('Update')
    

                 