from flask import Blueprint, render_template, url_for, request, flash, redirect, send_from_directory
from flask_login import login_required, login_user, logout_user, current_user

from sqlalchemy import text
from webdata.models import Pengguna
from webdata import db , bcrypt, app

artikel = Blueprint('artikel', __name__)

@artikel.route('/')
@login_required
def index():
    return render_template('artikel/artikel.html')

@artikel.route('/detail')
@login_required
def detail():
    return render_template('artikel/detail_artikel.html')