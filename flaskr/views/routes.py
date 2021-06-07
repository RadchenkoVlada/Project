from flask import current_app as app
from flask import render_template, redirect, url_for, request, flash
from flaskr.models import User, Location, Car
from flaskr.forms import LoginForm, SearchForm
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/search/loc/<int:location_id>/', methods=['GET'])
@app.route('/search/loc/<int:location_id>/page/', methods=['GET'])
@app.route('/search/loc/<int:location_id>/page/<int:page>', methods=['GET'])
def search(location_id, page=1):
    CARS_PER_PAGE = 10

    # page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Car.query.filter_by(ref_location=location_id).paginate(page, CARS_PER_PAGE, False)
    # pagination = Pagination(page=page, total=cars.count(), search=True, record_name='users')

    return render_template('search_page/search.html',
                           cars=pagination.items,
                           pagination=pagination,
                           location_id=location_id)



@app.route('/home/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.method)
    form = SearchForm()
    form.location.choices = [(str(l.id), l.name) for l in Location.query.all()]

    if form.validate_on_submit():
        if form.drop_off_date.data < form.pick_up_date.data:
            flash('Drop-Off date should be after Pick up', 'error')
            return redirect(url_for('home'))

        location = Location.query.get(int(form.location.data))
        if location:
            return redirect(url_for('search', location_id=location.id)) # TODO: add dates to url
        flash('Location not found', 'error')
        return redirect(url_for('home'))

    for field, errors in form.errors.items():
        flash(form[field].label.text + ": " + ", ".join(errors), 'error')

    return render_template('home.html', form=form)


@app.route('/about/')
def about():
    return render_template('about.html', title="About")


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


@app.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('home'))

