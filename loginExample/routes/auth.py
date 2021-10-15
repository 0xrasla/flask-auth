from flask import Blueprint, render_template, redirect, url_for, request
from flask.helpers import flash
from flask_bcrypt import Bcrypt
from loginExample import models, db

from flask_login import login_user, logout_user

brypt = Bcrypt()
auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        
        if(not models.User.authenticate(email=email, password=password)):
            flash("Please check your login details.....")
            return redirect(url_for("auth.login"))
            
        
        login_user(user=models.User.query.filter_by(email=email).first(), remember=remember)
        return redirect(url_for("home.main"))
    return render_template("login.htm", title="Login Page")


@auth.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        if (not models.User.userexists(email=email)):
            new_user = models.User(email=email, password=password, username=username)
            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for("auth.login"))
        
        else:
            flash("Email already taken......")
            return redirect(url_for("auth.signup"))
        
    return render_template("signup.htm", title="Signup Page", error="")

@auth.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("auth.login"))