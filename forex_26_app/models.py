
# ======= IS THERE =======

from datetime import datetime
from forex_26_app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

# ====================== ADMIN TABLE ============== 
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key = True)
    name = db.Column(db.String(28), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    
    posts = db.relationship("Post", backref="author", lazy = True)
    posts_signals = db.relationship("Post_Signals", backref="author", lazy = True)
    
    def __repr__(self):
        return f"Admin('{ self.name }')"
    
# ====================== POST TABLE ==============  
class Post(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key = True)
    image = db.Column(db.String(30), nullable=False, default = "default.jpg")
    title = db.Column(db.String(100), nullable=False)
    post = db.Column(db.Text, nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    
    user = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable = False)
    
    def __repr__(self):
        return f"Post('{ self.image }', '{ self.title }', '{ self.post }')"

# ====================== POST SIGNAL TABLE ==============    
class Post_Signals(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key = True)
    image = db.Column(db.String(30), nullable=False, default = "default.jpg")
    title = db.Column(db.String(100), nullable=False)
    post = db.Column(db.Text, nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    
    user = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable = False)
    
    def __repr__(self):
        return f"Post('{ self.image }', '{ self.title }', '{ self.post }')"

# ====================== FEEDBACK TABLE ==============     
class Feedback(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    
    def __repr__(self):
        return f"Post('{ self.name }', '{ self.email }', '{ self.subject }', '{ self.message }')"