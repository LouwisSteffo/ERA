from webdata import db, auth
from flask_login import UserMixin
from datetime import datetime
import locale

# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
@auth.user_loader
def load_user(user_id):
    return Pengguna.query.get(int(user_id)) 

class Pengguna(db.Model, UserMixin):
    __tablename__ = 'pengguna'
    id = db.Column(db.Integer, primary_key=True)
    nama_pengguna = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nomor_telepon = db.Column(db.String(20), unique=True, nullable=False)
    foto_profil = db.Column(db.String(100), nullable=True, default='default.jpg')
    alamat = db.Column(db.String(100), nullable=True)
    poin = db.Column(db.Integer, nullable=False, default=0)
    password = db.Column(db.String(300), nullable=False)
    
    def __repr__(self):
        return f"{self.nama_pengguna}', '{self.username}', '{self.email}', '{self.foto_profil}"
    
    def get_id(self):
        return str(self.id)
    
    
class Ekspedisi(db.Model , UserMixin):
    __tablename__ = 'ekspedisi'
    id = db.Column(db.Integer, primary_key=True)
    nama_ekspedisi = db.Column(db.String(100), nullable=False)
    
class LimbahElektronik(db.Model , UserMixin):
    __tablename__ = 'limbah_elektronik'
    id = db.Column(db.Integer, primary_key=True)
    nama_limbah = db.Column(db.String(100), nullable=False)
    gambar_limbah = db.Column(db.String(100), nullable=False, default='default.jpg')
    
class Lokasi(db.Model , UserMixin):
    __tablename__ = 'lokasi'
    id = db.Column(db.Integer, primary_key=True)
    nama_lokasi = db.Column(db.String(100), nullable=False)
    alamat_lokasi = db.Column(db.String(100), nullable=False)
    waktu_buka = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    waktu_tutup = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    gambar_lokasi = db.Column(db.String(100), nullable=False, default='default.jpg')
    
class Kupon(db.Model , UserMixin):
    __tablename__ = 'kupon'
    id = db.Column(db.Integer, primary_key=True)
    nama_kupon = db.Column(db.String(100), nullable=False)
    harga_kupon = db.Column(db.Integer, nullable=False)
    gambar_kupon = db.Column(db.String(100), nullable=False, default='default.jpg')
    jumlah_kupon = db.Column(db.Integer, nullable=False)
    
class Transaksi_Penjemputan(db.Model , UserMixin):
    __tablename__ = 'transaksi_penjemputan'
    id = db.Column(db.Integer, primary_key=True)
    id_pengguna = db.Column(db.Integer, db.ForeignKey('pengguna.id'), nullable=False)
    id_ekspedisi = db.Column(db.Integer, db.ForeignKey('ekspedisi.id'), nullable=True)
    id_lokasi = db.Column(db.Integer, db.ForeignKey('lokasi.id'), nullable=True)
    berat_limbah = db.Column(db.Integer, nullable=False)
    tanggal_transaksi = db.Column(db.DateTime , nullable=False , default=datetime.utcnow)
    status_transaksi = db.Column(db.String(100), nullable=False)
    
    @property
    def pengguna_detail(self):
        return Pengguna.query.filter_by(id=self.id_pengguna).first()
    
    @property
    def ekspedisi_detail(self):
        return Ekspedisi.query.filter_by(id=self.id_ekspedisi).first()
    
    @property
    def lokasi_detail(self):
        return Lokasi.query.filter_by(id=self.id_lokasi).first()
class Redeem(db.Model, UserMixin):
    _tablename_ = 'redeem'
    id = db.Column(db.Integer, primary_key=True)
    id_pengguna = db.Column(db.Integer, db.ForeignKey('pengguna.id'), nullable=False)
    id_kupon = db.Column(db.Integer, db.ForeignKey('kupon.id'), nullable=False)
    waktu_ditukar = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    @property
    def harga_kupon(self):
        return Kupon.query.filter_by(id=self.id_kupon).first()
    
    @property
    def poin_user(self):
        return Pengguna.query.filter_by(id=self.id).first()