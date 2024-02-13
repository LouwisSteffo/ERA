from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna
from webdata import db , bcrypt

user = Blueprint('user', __name__)

@user.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("User Logged out", "warning")
    return redirect(url_for('main.login'))

@user.route('/profile')
@login_required
def profile():
    return render_template('user/profile.html')

@user.route('/edit_profile')
@login_required
def edit_profile():
    return render_template('user/edit_profile.html')

@user.route('/edit' , methods=['POST'])
@login_required
def edit():
    user = Pengguna.query.filter_by(id=current_user.id).first()
    id = user.id
    username = request.form['username']
    email = request.form['email']
    nomor_telepon = request.form['nomor_telepon']
    alamat = request.form['alamat']
    
    validation = Pengguna.query.filter_by(email=email).first()
    if validation and validation.id != id:
        flash('Email sudah terdaftar', 'danger')
        return redirect(url_for('user.edit_profile'))
    
    validation = Pengguna.query.filter_by(nomor_telepon=nomor_telepon).first()
    if validation and validation.id != id:
        flash('Nomor telepon sudah terdaftar', 'danger')
        return redirect(url_for('user.edit_profile'))
    
    validation = Pengguna.query.filter_by(username=username).first()
    if validation and validation.id != id:
        flash('Username sudah terdaftar', 'danger')
        return redirect(url_for('user.edit_profile'))
    
    user.username = username
    user.email = email
    user.nomor_telepon = nomor_telepon
    user.alamat = alamat
    
    db.session.commit()

    flash('Profile berhasil diubah', 'success')
    return redirect(url_for('user.edit_profile'))

@user.route('/ganti_password')
@login_required
def ganti_password():
    return render_template('user/ubahpassword.html')

@user.route('/change' , methods=['POST'])
@login_required
def change():
    user = Pengguna.query.filter_by(id=current_user.id).first()
    passwordlama = request.form['passwordlama']
    passwordbaru = request.form['passwordbaru']
    konfirmasipassword = request.form['konfirmasipassword']
    
    if not passwordlama or not passwordbaru or not konfirmasipassword:
        flash('Data tidak boleh kosong', 'danger')
        return redirect(url_for('user.ganti_password'))
    
    if not bcrypt.check_password_hash(user.password, passwordlama):
        flash('Password salah', 'danger')
        return redirect(url_for('user.ganti_password'))
    
    
    if passwordbaru != konfirmasipassword:
        flash('Password tidak sama', 'danger')
        return redirect(url_for('user.ganti_password'))
    
    hashed_password = bcrypt.generate_password_hash(passwordbaru).decode('utf-8')
    user.password = hashed_password
    db.session.commit()
    
    flash('Password berhasil diubah', 'success')
    return redirect(url_for('user.edit_profile'))