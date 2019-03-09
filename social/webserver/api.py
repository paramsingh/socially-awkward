from flask import Blueprint, request, render_template
import social.db.user as db_user
import social.db.follow as db_follow
import json
from social.webserver.login import User
from flask_login import login_required, login_user, current_user, logout_user

api = Blueprint('api', __name__)

@api.route('/exist')
def user_exists():
	username = request.args.get("username")
	result = db_user.get_by_username(username)
	print username
	if result is None:
		return "Not Found", 404
	else:
		return "Found"

