from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna, Transaksi_Penjemputan
from webdata import db , bcrypt
from random import randint

penjemputan = Blueprint('penjemputan', __name__)
# simpan = {
#     "Layanan" : 0,
#     "Ekspedisi" : 1,
#     "Lokasi" : 0,
#     "Berat" : randint(1,10),
#     "Status" : "Sedang Diproses"
    
# }
@penjemputan.route('/')
@login_required
def index():
    return render_template('penjemputan/penjemputan.html')

@penjemputan.route('/pilih_layanan', methods=['GET', 'POST'])
@login_required
def pilih_layanan():

    if request.method == 'POST':
        layanan_pilihan = request.form.get('pilihan_layanan')
        simpan = layanan_pilihan
        
        if layanan_pilihan == '1':
            return redirect(url_for('penjemputan.antar_sendiri'))
        elif layanan_pilihan == '2':
            return redirect(url_for('penjemputan.ekspedisi'))

    return render_template('penjemputan/pilih_layanan.html')   

@penjemputan.route('/ekspedisi')
@login_required
def ekspedisi():
    return render_template('penjemputan/halaman_ekspedisi.html')

@penjemputan.route('/antar_sendiri')
@login_required
def antar_sendiri():
    return render_template('penjemputan/lokasi_pengepul.html')

@penjemputan.route('/tambah_transaksi')
@login_required
def tambah_transaksi():
    # transaksi = Transaksi_Penjemputan(
    #                 id_pengguna = current_user.id,
    #                 id_ekspedisi = 1
    #             )
    return render_template('penjemputan/lokasi_pengepul.html')