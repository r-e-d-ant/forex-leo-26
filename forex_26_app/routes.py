
# ======= IS THERE =======

from flask import render_template, redirect, url_for, request, flash
from datetime import datetime
from forex_26_app import app, db, bcrypt
from forex_26_app.forms import AdminForm, LoginForm, PostForm, UpdatePostForm, PostSignalForm, UpdatePostSignalForm
from forex_26_app.models import Admin, Post, Post_Signals, Feedback
from flask_login import login_user, current_user, logout_user, login_required
import os
from PIL import Image
import json
from urllib.request import urlopen
import sys

# -----------

RED = '\033[91m' # red font color in terminal
GREEN = '\033[92m' # green font color in terminal
reset = '\033[0m' # white font color in terminal

with open('etc/config.json') as config_file:
    config = json.load(config_file)

API_KEY = config.get('API_KEY')

if API_KEY == "":
    print(RED, "\nSorry, This can't work without the API key", GREEN ,"\nGo get one here : https://free.currencyconverterapi.com/free-api-key \n", reset)
    sys.exit(0)
    


# assign url
countries_url = "https://free.currconv.com/api/v7/countries?apiKey="+API_KEY

try:
    # open countries url and read it content
    with urlopen(countries_url) as response:
        source = response.read()
except:
    print(RED, "\nSorry, something went wrong, Maybe the API key is invalid or there is no internet connection.\n", reset)
    sys.exit(0)
 

countries_data = json.loads(source)
infos = dict()
for key, value in countries_data['results'].items():
    curr_id = value['currencyId']
    curr_name = value['currencyName']
    infos[curr_id] = curr_name

# -----------
# Login and Register codes

# --- Register
@app.route('/home/register', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if not current_user.is_authenticated:
        abort(403)
    
    form = AdminForm() # init form
    if form.validate_on_submit(): # check if all the forms requirements are passed
        current_admin = Admin.query.filter_by(name=form.name.data).first() # check if the admin is arleady there.
        if current_admin: # if the user is there
            password_hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8") # crypt the password
            current_admin.name = form.name.data # update the name
            current_admin.password = password_hash # update the password
            db.session.commit()
            return redirect(url_for('login'))
        else: # if the user is not there
            password_hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8") # crypt the password
            admin = Admin(name=form.name.data, password=password_hash) # add the new record in Admin table
            db.session.add(admin)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

# --- Login
@app.route('/home/login', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm() # init form
    if form.validate_on_submit(): # check if all the forms requirements are passed
        with open('etc/config.json') as config_file:
            config = json.load(config_file)
            
        admin = Admin.query.filter_by(name=form.name.data).first() # check if admin is there
        if admin and bcrypt.check_password_hash(admin.password, form.password.data): # if admin check is True and password is True
            login_user(admin) # login the user
            next_page = request.args.get('next') # get next page args
            flash(f"Welcome { admin.name }", "success")
            return redirect(next_page) if next_page else redirect(url_for('home'))
        
        if form.name.data == config.get('ADMIN_USER_NAME') and form.password.data == config.get('ADMIN_PASSWORD'):
            current_admin = Admin.query.filter_by(name=config.get('ADMIN_USER_NAME')).first() # check if the admin is arleady there.
            if current_admin: # if the user is there
                login_user(admin) # login the user
                next_page = request.args.get('next') # get next page args
                flash(f"Welcome { admin.name }", "success")
                return redirect(next_page) if next_page else redirect(url_for('home'))
        
            elif not current_admin: # if the user is not there
                password_hash = bcrypt.generate_password_hash(config.get('ADMIN_PASSWORD')).decode("utf-8") # crypt the password
                admin = Admin(name=config.get('ADMIN_USER_NAME'), password=password_hash) # add the new record in Admin table
                db.session.add(admin)
                db.session.commit()
                flash(f"Please try to login in again, To make sure is you", "warning")
                return redirect(url_for('login'))
        else:
            flash("There was an error, please check your name and password", 'danger')
    return render_template('login.html', title="Login", form=form)


# ====================== LOGOUT ROUTE ==============
@app.route('/logout')
@login_required
def logout():
    logout_user() # if logout button clicke, just logout the current user
    return redirect(url_for('login')) # redirect to login page



# ====================== HOME ROUTE ==============
@app.route('/')
@app.route('/home')
def home():
    date = datetime.utcnow() # get current date
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.posted_date.desc()).paginate(page=page, per_page=6) # query post by posted date.
    return render_template('home.html', title="Home", posts=posts, date=date)

# ====================== SIGNAL POSTS ROUTE ==============
@app.route('/signals')
def signals():
	date = datetime.utcnow() # get current date
	posts_signals = Post_Signals.query.order_by(Post_Signals.posted_date.desc()) # query signal post by date.
	return render_template('signals.html', title="Signals", posts_signals=posts_signals, date=date)


# ====================== SAVE PICTURE FUNCTION ==============
# image saving settings
def save_picture(form_picture):
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = _ + f_ext
    picture_path = os.path.join(app.root_path, 'static/photos', picture_filename)
    
    i = Image.open(form_picture)
    i.save(picture_path)
    
    return picture_filename
   
# # ====================== NEW POST ROUTE ==============

@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm() # GET FORM
    if form.validate_on_submit():
        ''''If all the form requirement are good execute codes below'''
        if form.image.data:
            picture_file = save_picture(form.image.data) # assign picture name to a variable
            post = Post(image=picture_file, title=form.title.data, post=form.post.data, author=current_user)
            db.session.add(post)
            db.session.commit()
            flash("successfully posted", "success")
            return redirect(url_for("home"))
        else:
            post = Post(title=form.title.data, post=form.post.data, author=current_user)
            db.session.add(post)
            db.session.commit()
            flash("successfully posted", "success")
            return redirect(url_for("home"))
    elif request.method == 'GET':
        form.date_posted.data = datetime.utcnow().strftime("%d-%m-%Y")
            
    return render_template('create_post.html', title="new post", form=form)


# ====================== CREATE POST IN SIGNALS ROUTE ==============

@app.route('/create_post_signals', methods=['GET', 'POST'])
@login_required
def create_post_signals():
    form = PostSignalForm()
    if form.validate_on_submit():
        if form.price_form.data:
            post = Post_Signals(
                signal_action=form.signal_action_form.data,
                currencies=form.currencies_form.data,
                profit=form.profit_form.data,
                loss=form.loss_form.data,
                price=form.price_form.data,
                author=current_user)
            db.session.add(post)
            db.session.commit()

            flash("successfully posted", "success")
            return redirect(url_for("signals"))
        else:
            post = Post_Signals(
                signal_action=form.signal_action_form.data,
                currencies=form.currencies_form.data,
                profit=form.profit_form.data,
                loss=form.loss_form.data,
                author=current_user)
            db.session.add(post)
            db.session.commit()

            flash("successfully posted", "success")
            return redirect(url_for("signals"))
    elif request.method == 'GET':
        form.date_posted.data = datetime.utcnow().strftime("%d-%m-%Y")
            
    return render_template('create_post_signals.html', title="new post signal", form=form)


# ====================== VIEW SPCIFIC POST ROUTE ==============
@app.route('/post/<string:post_title>/<int:post_id>', methods=['GET', 'POST'])
def post(post_title, post_id):
    admin_post = Post.query.filter_by(id=post_id).first()
    return render_template('post.html', title=f"{post_title}", admin_post=admin_post)


# ====================== VIEW SPECIFIC POST FROM SIGNALS ROUTE ==============
# @app.route('/signal-post/<string:signal_post_title>/<int:signal_post_id>', methods=['GET', 'POST'])
# def signal_post(signal_post_title, signal_post_id):
#     signal_admin_post = Post_Signals.query.filter_by(id=signal_post_id).first()
#     return render_template('post_signal.html', title=f"{signal_post_title}", signal_admin_post=signal_admin_post)

# ====================== CONTACT ROUTE ==============
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        usr_name = request.form['name']
        usr_email = request.form['email']
        usr_subject = request.form['subject']
        usr_message = request.form['message']
        # save contacts infos in db
        feedback = Feedback(name=usr_name, email=usr_email, subject=usr_subject, message=usr_message)
        db.session.add(feedback)
        db.session.commit()
        
        flash("Thank you for your feedback.", "info")
        return render_template('contact.html')
    return render_template('contact.html')


@app.route('/feedback')
@login_required
def feedback():
    feedbacks = Feedback.query.order_by(Feedback.posted_date.desc())
    return render_template('feedback.html', feedbacks=feedbacks)

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def update(post_id):
    post = Post.query.get(post_id)
    form = UpdatePostForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            post.image = picture_file
            post.title = form.title.data
            post.post = form.post.data
            db.session.commit()
            flash("Post updated successfully", "success")
            return redirect(url_for("home"))
        else:
            post.title = form.title.data
            post.post = form.post.data
            db.session.commit()
            flash("Post updated successfully", "success")
            return redirect(url_for("home"))
        
    elif request.method == 'GET':
        form.image.data = post.image
        form.title.data = post.title
        form.post.data = post.post
        form.date_posted.data = datetime.utcnow().strftime("%d-%m-%Y")
    return render_template('update_post.html', title="Update post learn forex", form=form)

@app.route('/update_signal/<int:post_id>', methods=['GET', 'POST'])
@login_required
def update_signal(post_id):
    post = Post_Signals.query.get(post_id)
    form = UpdatePostSignalForm()
    if form.validate_on_submit():
        post.signal_action = form.signal_action_form.data
        post.currencies = form.currencies_form.data
        post.profit = form.profit_form.data
        post.loss = form.loss_form.data
        post.price_form = form.price_form.data
        db.session.commit()
        flash("Post updated successfully", "success")
        return redirect(url_for("signals"))
        
    elif request.method == 'GET':
        form.signal_action_form.data = post.signal_action
        form.currencies_form.data = post.currencies
        form.profit_form.data = post.profit
        form.loss_form.data = post.loss
        form.price_form.data = post.price
        form.date_posted.data = datetime.utcnow().strftime("%d-%m-%Y")
        
    return render_template('update_post_signal.html', title="Update post signal", form=form)
        
@app.route('/delete/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
        
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully", "success")
    return redirect(url_for("home"))

@app.route('/delete_signal/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete_signal(post_id):
    post = Post_Signals.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
        
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully", "success")
    return redirect(url_for("signals"))

@app.route('/feedback/delete_feedback/<int:feedback_id>', methods=['GET', 'POST'])
@login_required
def delete_feedback(feedback_id):
    feedback = Feedback.query.get_or_404(feedback_id)
    db.session.delete(feedback)
    db.session.commit()
    flash("Feedback deleted successfully", "success")
    return redirect(url_for("feedback"))



@app.route("/currency-convert", methods=["GET", "POST"])
def currency_convert():
    result = 0
    rate = 0
    date = datetime.utcnow()
    if request.method == 'POST':
        amount = request.form['amount']
        if amount:
            _from = request.form['currencyID_from']
            to = request.form['currencyID_to']
            convert_url = "https://free.currconv.com/api/v7/convert?q="+_from+"_"+to+"&compact=ultra&apiKey="+API_KEY
            with urlopen(convert_url) as response:
                source = response.read()
                
            convert_data = json.loads(source)
            rate = convert_data[_from+"_"+to]
            formatted_rate = "{:,}".format((round(float(rate), 4)))

            result = round(float(amount) * float(rate), 2)
            result = "{:,}".format(int(result))
            
            print("Amount:", str(amount), "From:", str(_from), "To:", str(to))
            print(result)
            return render_template('currency_converter.html', infos=sorted(infos.items()), rate=formatted_rate, result=result, date=date, title="Currency converter")
    return render_template('currency_converter.html', title="Currency converter",  time=datetime.utcnow(), infos=sorted(infos.items()), rate=rate, result=result, date=date)
