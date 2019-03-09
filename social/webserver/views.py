from flask import Blueprint, request, render_template
import social.db.user as db_user
import social.db.follow as db_follow
import social.db.post as db_post
import json
from social.webserver.login import User
from flask_login import login_required, login_user, current_user, logout_user
import requests

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

@bp.route('/follow', methods=['GET', 'POST'])
@login_required
def follow():
    username = request.form.get('username')
    if request.method == 'POST' and username:
        if user_exists(username):
            db_follow.add(current_user.id, username)
            return "Started following"
        else:
            return "User Not found"
    return render_template('follow.html')


@bp.route('/post', methods=['GET', 'POST'])
def post():
    post = request.form.get('post')
    if request.method == 'POST' and post:
        post_msg = db_post.create_post(current_user.id, post)
        return json.dumps(post_msg, indent=4)
    return render_template("post.html")


def split(username):
    name, server = username.split('@')
    print name
    return name, server


def user_exists(username):
    username, servername = split(username)
    r = requests.get("http://" + servername+"/api/exist", params={'username': username})
    return r.status_code == 200


def get_posts():
    if _get_post():
        # fetch the posts and show


def _get_post(username):
    username, servername = split(username)
    r = requests.get("http://" + servername + "/api/posts", params={'username': username})
    return r.status_code == 200
