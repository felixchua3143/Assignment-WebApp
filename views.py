from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
import shelve
from models import User  # Import User from models.py

views = Blueprint('views', __name__)

DATABASE_FILE = "database.db"


@views.route('/')
def home():
    return redirect(url_for('views.login'))


@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with shelve.open(DATABASE_FILE) as db:
            if username in db:
                flash("Username already exists!", "danger")
            else:
                db[username] = {'username': username, 'password': password}
                flash("Account created successfully!", "success")
                return redirect(url_for('views.login'))

    return render_template('signup.html', title="Sign Up")


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with shelve.open(DATABASE_FILE) as db:
            user_data = db.get(username)
            if user_data and user_data['password'] == password:
                user = User(id=username, username=user_data['username'], password=user_data['password'])
                login_user(user)
                flash("Logged in successfully!", "success")
                return redirect(url_for('views.profile'))
            else:
                flash("Invalid credentials!", "danger")

    return render_template('login.html', title="Log In")


@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title="Profile", username=current_user.username)


@views.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", "success")
    return redirect(url_for('views.login'))


@views.route('/delete', methods=['POST'])
@login_required
def delete_account():
    with shelve.open(DATABASE_FILE) as db:
        del db[current_user.id]
    logout_user()
    flash("Account deleted successfully!", "success")
    return redirect(url_for('views.signup'))


@views.route('/update', methods=['GET', 'POST'])
@login_required
def update_account():
    if request.method == 'POST':
        new_username = request.form['username']
        new_password = request.form['password']

        with shelve.open(DATABASE_FILE) as db:
            if new_username in db and new_username != current_user.id:
                flash("Username already exists!", "danger")
            else:
                del db[current_user.id]
                db[new_username] = {'username': new_username, 'password': new_password}
                logout_user()
                flash("Account updated. Please log in again.", "success")
                return redirect(url_for('views.login'))

    return render_template('profile.html', title="Update Account")