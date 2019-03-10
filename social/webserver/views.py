from __future__ import print_function
from flask import Blueprint, request, render_template, jsonify, current_app
import social.db.user as db_user
import social.db.follow as db_follow
import social.db.post as db_post
import json
from social.webserver.login import User
from flask_login import login_required, login_user, current_user, logout_user
import requests
from werkzeug.exceptions import NotFound

bp = Blueprint('bp', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@bp.route('/signup', methods=['GET', 'POST'])
def sign_up():
    username = request.form.get('username')
    password = request.form.get('password')
    if request.method == 'POST' and username and password:
        try:
            user = db_user.create_user(username, password)
        except Exception as e:
            print(str(e))
            return "There was an error while creating the user", 500
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
@login_required
def post():
    post = request.form.get('post')
    if request.method == 'POST' and post:
        post_msg = db_post.create_post(current_user.id, post)
        return json.dumps(post_msg, indent=4)
    return render_template("post.html")

@bp.route('/user/<user_name>', methods=['GET'])
def profile(user_name):
    try:
        posts = _get_posts(user_name)
        return jsonify(posts)
    except NotFound:
        return "user not found", 404
    except Exception:
        return "There was an error", 500


def split(username):
    split = username.split('@')
    if len(split) == 2:
        name, server = split
    elif len(split) == 1:
        name = split[0]
        server = current_app.config['CURRENT_SERVER']
    return name, server


def user_exists(username):
    username, servername = split(username)
    r = requests.get("http://" + servername+"/api/exist", params={'username': username})
    return r.status_code == 200


def _get_posts(username):
    username, servername = split(username)
    r = requests.get("http://" + servername + "/api/posts", params={'username': username})
    if r.status_code == 404:
        raise NotFound
    elif r.status_code != 200:
        raise ExternalServerError
    else:
        return r.json()

class ExternalServerError(Exception):
    pass
