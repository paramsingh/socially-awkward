from flask import Blueprint, request, render_template
import social.db.user as db_user
import json
from social.webserver.login import User
from flask_login import login_required, login_user, current_user, logout_user

bp = Blueprint('bp', __name__)

@bp.route('/signup', methods=['GET', 'POST'])
def sign_up():
    username = request.form.get('username')
    password = request.form.get('password')
    if request.method == 'POST' and username and password:
        user = db_user.create_user(username, password)
        return json.dumps(user, indent=4)
    return render_template("signup.html")

# TODO: login forbidden
@bp.route('/login', methods=['GET', 'POST'])
def log_in():
    username = request.form.get('username')
    password = request.form.get('password')
    if request.method == 'POST' and username and password:
        user_id = db_user.get_by_username_and_password(username, password)
        if user_id is None:
            return "Incorrect Username or Password!"
        login_user(User(user_id))
        return "You've been logged in!"
    return render_template("login.html")

@bp.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    return "Logged out"

@bp.route('/only')
@login_required
def only_logged_in():
    return current_user.id