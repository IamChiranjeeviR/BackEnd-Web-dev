from flask import render_template, request, redirect, url_for, flash
from flask_package.forms import loginForm, registrationForm
from flask_package.models import User
from flask_package import app,db,bcrypt
from datetime import datetime
from flask_login import login_user

# Use the app context to create the database tables
with app.app_context():
    db.create_all()
    
fdbk = []

def store_feed(url):
    fdbk.append(dict(
        url = url,
        name = 'Chiru',
        date = datetime.utcnow()
    ))

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(EmailId = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('ins'))
        else:
            flash("Invalid Email or password")
    return render_template('login.html', title = 'Login', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = registrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(userName=form.userName.data,EmailId = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful :)')
        return redirect(url_for('login'))
    if form.errors:
        flash('Validation Errors:'+ str(form.errors))
        app.logger.error('Validation errors:'+ str(form.errors))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/ins")
def ins():
    return "Successfully Logged in"

@app.route("/feedBack", methods=['GET','POST'])
def feedBack():
    if request.method == "POST":
        url = request.form.get('url')
        store_feed(url)
        app.logger.debug('Stored Feedback: ' + url)
        flash("Thanks for Your Feedback :)")
        return redirect(url_for('home'))
    
    return render_template('feedBack.html') 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
