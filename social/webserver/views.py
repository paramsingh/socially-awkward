from flask import Blueprint, request, render_template
import social.db.user as db_user
import json

bp = Blueprint('bp', __name__)

@bp.route('/signup', methods=['GET', 'POST'])
def sign_up():
    username = request.form.get('username')
    password = request.form.get('password')
    if request.method == 'POST' and username and password:
        user = db_user.create_user(username, password)
        return json.dumps(user, indent=4)
    return render_template("signup.html")
