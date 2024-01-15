from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from logging import DEBUG
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

@app.route("/login")
def login():
    return render_template('login.html')

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