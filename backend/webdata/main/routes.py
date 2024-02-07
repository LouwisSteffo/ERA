from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from flask_login import login_required, login_user, logout_user
# from main.forms import LoginForm, RegisterForm
from webdata.models import Pengguna
from webdata import db , bcrypt

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('main/index.html')


# @main.route('/login' , methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         flash('Anda sudah login', 'info')
#         return redirect(url_for('main/loginregister.html'))
    
    # form = LoginForm()
    
    # if request.method == 'POST':
    #     if form.validate_on_submit():
    #         user = Pengguna.query.filter_by(email=form.email.data).first()
    #         if user and bcrypt.check_password_hash(user.password, form.password.data):
    #             login_user(user)
    #             flash('Login berhasil', 'success')
    #             # return redirect(url_for('.home'))
    #         else:
    #             flash('Login gagal. Cek kembali email dan password', 'danger')