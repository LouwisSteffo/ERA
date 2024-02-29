# from flask import Flask
# from webdata.models import db
# from webdata.config import Config
# from flask_sqlalchemy import SQLAlchemy

# from webdata import app , db , bcrypt
# from webdata.models import Pengguna, Ekspedisi, LimbahElektronik, Lokasi, Kupon, Transaksi_Penjemputan
# from datetime import datetime

# def main():
#     Lokasi1 = Lokasi(id = 1 , nama_lokasi="Pengepul Barang Rongsokan Limbah Elektronik Barang Bekas Loak" , alamat_lokasi="Jl. Ledeng, RT.04/RW.03, Gunungbatu, Kec. Bogor Bar, Kota Bogor, Jawa Barat" )
#     db.session.add(Lokasi1)
#     db.session.commit()
    
# if __name__ == '__main__':
#     with app.app_context():
#         main()