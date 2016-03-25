from functools import wraps
from logging import DEBUG
from logging.handlers import RotatingFileHandler
from flask import Flask, flash, redirect, render_template,\
     request, session, url_for, g

from forms import LoginForm, RegisterForm
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config.from_object('__config')
db = SQLAlchemy(app)

from models import User
import datetime

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args,  **kwargs)
        else:
            flash('You need to login first !!!')
            app.logger.info('%s' % datetime.datetime.now() + ' [INFO]' + ': Need to login first')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('name', None)
    flash('You logged out')
    app.logger.info('%s' % datetime.datetime.now() + ' [INFO]'+ ': The user logged out')
    return redirect(url_for('login'))

@app.route('/register/', methods=['GET','POST'])
def register():
    error = None
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        new_user = User(form.name.data,
                            form.email.data,
                            form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering. Please Login.')
            app.logger.info('%s' % datetime.datetime.now() + ' [INFO]'+ ': The user registered a user account with the user name of ' \
                    + form.name.data)
            return redirect(url_for('login'))
        except IntegrityError:
            error = 'The username and/or email already exist.'
            app.logger.error('%s' % datetime.datetime.now() + ' [ERROR]'+ ': ' + error)
            return render_template('register.html', form = form, error = error)
    return render_template('register.html', form = form, error = error)
    

@app.route('/')
def template():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name = request.form['name']).first()
            if user is not None and user.password == request.form['password']:
                session['logged_in'] = True
                session['user_id'] = user.id
                session['name'] = user.name
                app.logger.info('%s' % datetime.datetime.now() + ' [INFO]'+ ': '+ request.form['name'] + ' is logged in to the system')
                return redirect(url_for('template'))
            else:
                error = 'Invalid Credentials. Please try again.'
                app.logger.error('%s' % datetime.datetime.now() + ' [ERROR]'+ ': ' + error)
        else:
            error = 'Both fields are required'
            app.logger.error('%s' % datetime.datetime.now() + ' [ERROR]' + ': ' + error)
    return render_template('login.html', form = form, error = error)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr (form, field).label.text, error), 'error')
