from flask import Blueprint, request, render_template, jsonify
import social.db.user as db_user
import social.db.follow as db_follow
import social.db.post as db_post
import json
from social.webserver.login import User
from flask_login import login_required, login_user, current_user, logout_user

api = Blueprint('api', __name__)

@api.route('/exist')
def user_exists():
    username = request.args.get("username")
    result, val = db_user.get_by_username(username)
    if result is None:
        return "Not Found", 404
    else:
        return "Found"


@api.route('/posts')
def get_posts():
    username = request.args.get("username")
    user_id, user_name = db_user.get_by_username(username)
    if user_id is None:
        return jsonify({"message": "Not Found"}), 404

    posts = db_post.get_posts(user_id)
    return jsonify(posts)

