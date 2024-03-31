from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField , PasswordField , BooleanField , ValidationError 
from wtforms.validators import DataRequired , EqualTo , Length
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField

#create a form class
class UserForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    username = StringField("username" , validators=[DataRequired()])
    email = StringField("Email",validators = [DataRequired()])
    hometown = StringField("HomeTown", validators=[DataRequired()])
    profile_pic = FileField("profile pic")
    password_hash = PasswordField('Password' , validators = [DataRequired(), EqualTo('password_hash2', message = 'Passwords must match')])
    password_hash2 =  PasswordField('Comfirm password', validators = [DataRequired()] )
    submit = SubmitField("Sign Up")

#update class form
class UpdateForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    username = StringField("username", validators=[DataRequired()])
    email = StringField("Email",validators = [DataRequired()])
    hometown = StringField("HomeTown",validators= [DataRequired()])
    profile_pic = FileField("profile pic")
    password_hash = PasswordField('Password' , validators = [DataRequired(), EqualTo('password_hash2', message = 'passwords must match')])
    password_hash2 =  PasswordField('Comfirm password', validators = [DataRequired()] )
    update = SubmitField("update")

#create a form class
class namerform(FlaskForm):
    name = StringField("Your name", validators = [DataRequired()])
    submit = SubmitField("Submit")

#create a password form
class PasswordForm(FlaskForm):
    email = StringField("Your email?", validators = [DataRequired()])
    password_hash = PasswordField("whats your password?",validators=[DataRequired()])
    submit = SubmitField("Submit")

#create a posts form
class PostForm(FlaskForm):
        shopname = StringField("shopname", validators=[DataRequired()] )
        content = CKEditorField("content" , validators = [DataRequired()])
        #content = StringField("content",validators=[DataRequired()],widget = TextArea())
        shopowner = StringField("shopowner")
        address = StringField("address",validators=[DataRequired()])
        contact = StringField("contact",validators= [Length(min=10, max=10, message="Telephone should be 10 digits (no spaces)")])
        slug = StringField("slug")
        submit = SubmitField("Submit")

#create login form
class LoginForm(FlaskForm):
      username = StringField("username", validators=[DataRequired()])
      password = PasswordField("password",validators=[DataRequired()])
      submit = SubmitField("Login")

#create a search form
class SearchForm(FlaskForm):
     searched = StringField("searched",validators=[DataRequired()])
     submit = SubmitField("Submit")
     