from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna
from webdata import db , bcrypt

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('main/index.html')

@main.route('/login')
def login():
    return render_template('main/loginregister.html')

@main.route('/signuppost',  methods=['POST'])
def signuppost():
    username = request.form['username']
    nama = request.form['nama']
    nomor_telepon = request.form['nomor_telpon']
    email = request.form['email']
    password = request.form['password']
    
    if len(username) > 20:
        flash('Username tidak boleh lebih dari 20 karakter', 'danger')
        return redirect(url_for('main.login'))
    

    if not username or not nama or not nomor_telepon or not email or not password:
        flash('Data tidak boleh kosong', 'danger')
        return redirect(url_for('main.login'))
    
    print(username, nama, nomor_telepon, email, password)
    
    check = Pengguna.query.filter_by(email=email).first()
    
    if check: 
        flash('Email sudah terdaftar', 'danger')
        return redirect(url_for('main.login'))
    
    check = Pengguna.query.filter_by(nomor_telepon=nomor_telepon).first()
    
    if check:
        flash('Nomor telepon sudah terdaftar', 'danger')
        return redirect(url_for('main.login'))
    
    check = Pengguna.query.filter_by(username=username).first()
    
    if check:
        flash('Username sudah terdaftar', 'danger')
        return redirect(url_for('main.login'))
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    new_user = Pengguna(username=username, nama_pengguna=nama, email=email, nomor_telepon=nomor_telepon, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    flash('Akun berhasil dibuat Silahkan login terlebih dahulu', 'success')
    
    return redirect(url_for('main.login'))
    
@main.route('/loginpost', methods=['POST'])
def loginpost():
    email = request.form['email']
    password = request.form['password']
    
    if not email or not password:
        flash('Data tidak boleh kosong', 'danger')
        return redirect(url_for('main.login'))
    
    user = Pengguna.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        flash('Login berhasil', 'success')
        return redirect(url_for('main.home'))
    
    flash('Login gagal. Cek kembali email dan password', 'danger')
    return redirect(url_for('main.login'))
