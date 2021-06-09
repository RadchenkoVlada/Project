from flask import current_app as app
from flaskr import db
from flask import render_template, redirect, url_for, request, flash

from flaskr.models import User, Location, Car
from flaskr.forms import LoginForm, RegistrationForm, SearchForm
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/search/loc/<int:location_id>/', methods=['GET'])
@app.route('/search/loc/<int:location_id>/page/', methods=['GET'])
@app.route('/search/loc/<int:location_id>/page/<int:page>/', methods=['GET'])
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
        # TODO: Add addtional check. pick_up_date can't be before today

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

    return render_template('login.html', title='Login', form=form)


@app.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('home'))


@app.route('/user_registration/', methods=['GET', 'POST'])
def registration():
    """User register logic."""
    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user_by_email = User.query.filter_by(email=form.email.data).first()
        existing_user_by_phone = User.query.filter_by(phone_number=form.phone_number.data).first()
        if existing_user_by_email is not None or existing_user_by_phone is not None:
            flash('A user already exists with that email address or phone number.', 'error')
        else:
            user = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                phone_number=form.phone_number.data,
                email=form.email.data,
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            flash(f'Registration Successful. Thank you {form.first_name.data} for registering.', 'success')

            return redirect(url_for('home'))

    for field, errors in form.errors.items():
        flash(form[field].label.text + ": " + ", ".join(errors), 'error')

    return render_template('user_registration.html', title='Register', form=form)


@app.route('/car_details/<int:car_id>/')
def car_details(car_id):
    car = Car.query.get(car_id)
    if car:
        return render_template('car_details.html', title="Car Details", car=car)
    else:
        flash('Car not found', 'error')
        return redirect(request.referrer or url_for('home'))
