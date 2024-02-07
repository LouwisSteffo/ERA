# from flask import Flask
# from webdata.models import db
# from webdata.config import Config
# from flask_sqlalchemy import SQLAlchemy

# from webdata import app , db , bcrypt
# from webdata.models import Pengguna, Ekspedisi, LimbahElektronik, Lokasi, Kupon, Transaksi_Penjemputan

# def main():
#     Pengguna1 = Pengguna(nama_pengguna='Lous', username='admin', email='lou@gmail.com' , nomor_telepon='08123456789', alamat='Jl. Kebon Jeruk No. 1', password=bcrypt.generate_password_hash('admin').decode('utf-8'))
#     db.session.add(Pengguna1)
#     db.session.commit()
    
# if __name__ == '__main__':
#     with app.app_context():
#         main()