from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna, Transaksi_Penjemputan , Ekspedisi
from webdata import db , bcrypt

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
@login_required
def index():
    count1 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dalam Antrean').count()
    count2 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dalam Proses').count()
    count3 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Selesai').count()
    count4 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dibatalkan').count()
    list_transaksi = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dalam Antrean').all()
    total = len(list_transaksi)
    return render_template('dashboard/dashboard_dalam_antrean.html', list_transaksi=list_transaksi, count1=count1, count2=count2, count3=count3, count4=count4, total=total)

@dashboard.route('/dalam_proses')
@login_required
def dalam_proses():
    count1 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dalam Antrean').count()
    count2 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dalam Proses').count()
    count3 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Selesai').count()
    count4 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dibatalkan').count()
    list_transaksi = Transaksi_Penjemputan.query.filter_by(status_transaksi = 'Dalam Proses').all()
    total = len(list_transaksi)
    return render_template('dashboard/dashboard_dalam_proses.html', list_transaksi = list_transaksi, total=total , count1=count1, count2=count2, count3=count3, count4=count4)

@dashboard.route('/selesai')
@login_required
def selesai():
    count1 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dalam Antrean').count()
    count2 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dalam Proses').count()
    count3 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Selesai').count()
    count4 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dibatalkan').count()
    list_transaksi = Transaksi_Penjemputan.query.filter_by(status_transaksi = 'Selesai').all()
    total = len(list_transaksi)
    return render_template('dashboard/dashboard_selesai.html', list_transaksi = list_transaksi, total=total , count1=count1, count2=count2, count3=count3, count4=count4)

@dashboard.route('/batal')
@login_required
def batal():
    count1 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dalam Antrean').count()
    count2 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dalam Proses').count()
    count3 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Selesai').count()
    count4 = Transaksi_Penjemputan.query.filter_by(status_transaksi='Dibatalkan').count()
    list_transaksi = Transaksi_Penjemputan.query.filter_by(status_transaksi = 'Dibatalkan').all()
    total = len(list_transaksi)
    return render_template('dashboard/dashboard_pembatalan.html', list_transaksi = list_transaksi, total=total , count1=count1, count2=count2, count3=count3, count4=count4)

@dashboard.route('/membatalkan/<int:id>')
@login_required
def membatalkan(id):
    transaksi = Transaksi_Penjemputan.query.filter_by(id=id).first()
    
    transaksi.status_transaksi = 'Dibatalkan'
    db.session.commit()
    flash('Transaksi berhasil dibatalkan', 'warning')
    return redirect(url_for('dashboard.dalam_proses'))

@dashboard.route('/membatal/<int:id>')
@login_required
def membatal(id):
    transaksi = Transaksi_Penjemputan.query.filter_by(id=id).first()
    
    transaksi.status_transaksi = 'Dibatalkan'
    db.session.commit()
    flash('Transaksi berhasil dibatalkan', 'warning')
    return redirect(url_for('dashboard.index'))