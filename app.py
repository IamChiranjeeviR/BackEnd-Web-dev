from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from logging import DEBUG
from forms import loginForm, registrationForm

app = Flask(__name__)

app.logger.setLevel(DEBUG)
app.secret_key = b'x\x12\x1cM\xe5@\x97\xb0'
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
        if form.email.data == 'iamchiranjeeviramakrishna@gmail.com' and form.password.data == 'chiru123':
            flash("Logged in Successfully :)")
            return redirect(url_for('home'))
        else:
            flash("Invalid Email or password")
    return render_template('login.html', title = 'Login', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = registrationForm()
    if form.validate_on_submit():
        flash('Registration Successful :)')
        return redirect(url_for('login'))
    if form.errors:
        flash('Validation Errors:'+ str(form.errors))
        app.logger.error('Validation errors:'+ str(form.errors))
    return render_template('register.html', title = 'Register', form = form)

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

if __name__ == "__main__":
    app.run(debug=True)