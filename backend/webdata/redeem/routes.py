from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna
from webdata import db , bcrypt

redeem = Blueprint('redeem', __name__)

@redeem.route('/')
def index():
    return render_template('redeem/redeem.html')
