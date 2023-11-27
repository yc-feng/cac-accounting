from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .models import User
from .util import get_users, get_transitions, get_inventory

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # User validation logic
        user = User.get(username)
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.transition'))  # Redirect to a protected page

        flash('Invalid username or password')

    return render_template('login.html')

@main.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')

# Transition Records Route
@main.route('/transition')
@login_required
def transition():
    data = get_transitions()
    return render_template('transition.html', data=data)

# Inventory Route
@main.route('/inventory')
@login_required
def inventory():
    data = get_inventory()
    return render_template('inventory.html', data=data)

@main.route("/cronjob")
def test():
  return "Successful"