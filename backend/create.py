# from flask import Flask
# from webdata.models import db
# from webdata.config import Config
# from flask_sqlalchemy import SQLAlchemy

# from webdata import app , db , bcrypt
# from webdata.models import Pengguna, Ekspedisi, LimbahElektronik, Lokasi, Kupon, Transaksi_Penjemputan
# from datetime import datetime

# def main():
#     Lokasi1 = Lokasi(id = 1 , nama_lokasi="Pengepul Barang Rongsokan Limbah Elektronik Barang Bekas Loak" , alamat_lokasi="Jl. Ledeng, RT.04/RW.03, Gunungbatu, Kec. Bogor Bar, Kota Bogor, Jawa Barat" )
#     Lokasi2 = Lokasi(id = 2 , nama_lokasi="Gudang Rongsokan Barang Bekas & Limbah Elektronik" , alamat_lokasi="Jl. Bogor Nirwana Residence, RT.01/RW.10, Ranggamekar, Kec. Bogor Sel., Kota Bogor, Jawa Barat" )
#     Lokasi3 = Lokasi(id = 3 , nama_lokasi="Gudang UD Jaya Abadi Scrapindo Pengepul Besi Tua Barang Bekas Loak & Limbah Elektronik Bogor" , alamat_lokasi="Jl. Kp. Sawah Kaum, RT.03 RW02/RW.09, Mekarjaya, Kec. Ciomas, Kabupaten Bogor, Jawa Barat 16610" )
#     Lokasi4 = Lokasi(id = 4 , nama_lokasi="Lapak Rongsok Barang Bekas & Limbah Elektronik Akar Makmur" , alamat_lokasi="Muara sari, RT.01/RW.12, Pasirkuda, Kec. Bogor Bar., Kota Bogor, Jawa Barat 16119" )
    
#     Ekspedisi1 = Ekspedisi(id = 1, nama_ekspedisi = "JNE")
#     Ekspedisi2 = Ekspedisi(id = 2, nama_ekspedisi = "J&T Express")
#     Ekspedisi3 = Ekspedisi(id = 3, nama_ekspedisi = "GrabExpress")
#     Ekspedisi4 = Ekspedisi(id = 4, nama_ekspedisi = "Gosend")
    
#     db.session.add(Lokasi1)
#     db.session.add(Lokasi2)
#     db.session.add(Lokasi3)
#     db.session.add(Lokasi4)
    
#     db.session.add(Ekspedisi1)
#     db.session.add(Ekspedisi2)
#     db.session.add(Ekspedisi3)
#     db.session.add(Ekspedisi4)
    
#     db.session.commit()
    
# if __name__ == '__main__':
#     with app.app_context():
#         main()