from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna, Transaksi_Penjemputan , Ekspedisi
from webdata import db , bcrypt

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def index():
    list_transaksi = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dalam Antrean').all()
    total = len(list_transaksi)
    return render_template('dashboard/dashboard_dalam_antrean.html', list_transaksi=list_transaksi, total=total)

@dashboard.route('/dalam_proses')
@login_required
def dalam_proses():
    list_transaksi = Transaksi_Penjemputan.query.filter_by(status_transaksi = 'Dalam Proses').all()
    total = len(list_transaksi)
    return render_template('dashboard/dashboard_dalam_proses.html', list_transaksi = list_transaksi, total=total)

@dashboard.route('/selesai')
@login_required
def selesai():
    list_transaksi = Transaksi_Penjemputan.query.filter_by(status_transaksi = 'Selesai').all()
    total = len(list_transaksi)
    return render_template('dashboard/dashboard_selesai.html', list_transaksi = list_transaksi, total=total)

@dashboard.route('/batal')
@login_required
def batal():
    list_transaksi = Transaksi_Penjemputan.query.filter_by(status_transaksi = 'Dibatalkan').all()
    total = len(list_transaksi)
    return render_template('dashboard/dashboard_pembatalan.html', list_transaksi = list_transaksi, total=total)