from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
    'author': 'Faruq Tee',
    'title': 'i did not see it coming',
    'content': 'First Blog post',
    'date_posted': 'September 12 2022'
    },
    {
    'author': 'Faruq Tee',
    'title': 'Once upon a time',
    'content': 'Second Blog post',
    'date_posted': 'September 16 2022'
    }
]

@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)