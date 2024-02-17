from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna
from webdata import db , bcrypt

penjemputan = Blueprint('penjemputan', __name__)

@penjemputan.route('/')
@login_required
def index():
    return render_template('penjemputan/penjemputan.html')

@penjemputan.route('/pilih_layanan')
@login_required
def pilih_layanan():
    return render_template('penjemputan/pilih_layanan.html')