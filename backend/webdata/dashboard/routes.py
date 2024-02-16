from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna
from webdata import db , bcrypt

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def index():
    return render_template('dashboard/dashboard_dalam_antrean.html')