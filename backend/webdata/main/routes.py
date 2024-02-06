from flask import Blueprint, render_template, url_for, request, flash, redirect
# from flask_login import login_required, login_user, logout_user, current_user
# from sqlalchemy import text
# from flask_login import login_required, login_user, logout_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/loginregister.html')