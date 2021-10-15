from flask import Blueprint, render_template
from flask_login import login_required, current_user

route = Blueprint("home", __name__, url_prefix="/home")


@route.route("/")
@login_required
def main():
    return render_template("home.htm", user=current_user, title="Blog Home")
