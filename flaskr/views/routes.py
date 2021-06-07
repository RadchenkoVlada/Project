from flask import current_app as app
from flask import render_template, redirect, url_for, request, flash
from flaskr.models import User
from flaskr.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/home/')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.
    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            flash('Logged in successfully', 'success')
            login_user(user)
            next_page = request.args.get('next')
            return redirect(url_for('home'))
        flash('Invalid username/password combination', 'error')
        return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('home'))
