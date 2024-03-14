from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna, Transaksi_Penjemputan, Ekspedisi, Lokasi
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
    ekspedisi = Ekspedisi.query.all()
    # print(list_ekspedisi, end='\n\n\n')
    return render_template('penjemputan/halaman_ekspedisi.html', ekspedisi = ekspedisi)

@penjemputan.route('/antar_sendiri')
@login_required
def antar_sendiri():
    lokasi = Lokasi.query.all()
    return render_template('penjemputan/lokasi_pengepul.html', lokasi = lokasi)

@penjemputan.route('/tambah_transaksi/<int:id_ekspedisi>/<int:id_lokasi>', methods=['GET', 'POST'])
@login_required
def tambah_transaksi(id_ekspedisi, id_lokasi):
    
    # Antar Sendiri
    if id_ekspedisi == 0:
        transaksi = Transaksi_Penjemputan(
                        id_pengguna = current_user.id,
                        id_lokasi = id_lokasi,
                        berat_limbah = randint(1,10),
                        status_transaksi = 'Dalam Proses'
                    )
    # Penjemputan (Ekspedisi)
    else:
        transaksi = Transaksi_Penjemputan(
                        id_pengguna = current_user.id,
                        id_ekspedisi = id_ekspedisi,
                        berat_limbah = randint(1,10),
                        status_transaksi = 'Dalam Antrean'
                    )
    
    poin = transaksi.berat_limbah * 2
    print(poin)
    current_user.poin = current_user.poin + poin
    print(current_user.poin)
    
    db.session.add(transaksi)
    db.session.commit()
    
    # Flashnya g keluar
    flash('Transaksi Berhasil', 'success')
    
    if id_ekspedisi == 0:
        return redirect(url_for('dashboard.dalam_proses'))
    else:
        return redirect(url_for('dashboard.index'))