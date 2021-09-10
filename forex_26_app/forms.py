
# ======= IS THERE =======

from forex_26_app.models import Admin, Post, Post_Signals
from forex_26_app import bcrypt
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


# ====================== ADMIN FORM ============== 

class AdminForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=28)])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo("password")])

    save_button = SubmitField("Save")
    
    def validate_name(self, name):
        admin = Admin.query.filter_by(name=name.data).first()
        if admin:
            raise ValidationError("The name is the same with the current one, Please choose diferent.")

# ====================== LOGIN FORM ==============      
class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    
    login_button = SubmitField("Login")
    
    def validate_name(self, name):
        admin = Admin.query.filter_by(name=name.data).first()
        if not Admin:
            raise ValidationError("You can't login. Please check your name and password.")
        

# ====================== POST FORM ============== 
class PostForm(FlaskForm):
    image = FileField("Photo", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    title = StringField("Title", validators=[DataRequired(), Length(min=5, max=100)])
    post = TextAreaField("Main post", validators=[DataRequired(), Length(min=10)])
    date_posted = StringField("Date", validators=[DataRequired()])

    post_button = SubmitField("Post")
    
    def validate_title(self, title):
        postTitle = Post.query.filter_by(title=title.data).first()
        if postTitle:
            raise ValidationError("Sorry, Title similar to this is already posted.")

# ====================== UPDATE FORM ==============    
class UpdatePostForm(FlaskForm):
    image = FileField("Photo", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    title = StringField("Title", validators=[DataRequired(), Length(min=5, max=100)])
    post = TextAreaField("Main post", validators=[DataRequired(), Length(min=10)])
    date_posted = StringField("Date", validators=[DataRequired()])

    post_button = SubmitField("Update")
    

# ====================== SIGNAL POST FORM ============== 
class PostSignalForm(FlaskForm):
    signal_action_form = StringField("Signal Action", validators=[DataRequired(), Length(min=1, max=50)])
    currencies_form = StringField("currencies", validators=[DataRequired(), Length(min=1, max=50)])
    profit_form = StringField("Take a Profit", validators=[DataRequired(), Length(min=1, max=50)])
    loss_form = StringField("Stop Loss", validators=[DataRequired(), Length(min=1, max=50)])
    price_form = StringField("price(Optional)", validators=[DataRequired(), Length(min=1, max=50)])
    date_posted = StringField("Open at", validators=[DataRequired()])
    
    post_button = SubmitField("Post")

# ====================== UPDATE SIGNAL POST FORM ==============         
class UpdatePostSignalForm(FlaskForm):
    image = FileField("Photo", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    title = StringField("Title", validators=[DataRequired(), Length(min=5, max=100)])
    post = TextAreaField("Main post", validators=[DataRequired(), Length(min=10)])
    date_posted = StringField("Date", validators=[DataRequired()])
    
    post_button = SubmitField("Update")



