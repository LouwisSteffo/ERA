from flask import Blueprint, render_template, url_for, request, flash, redirect
from werkzeug.utils import secure_filename
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna
from webdata import db , bcrypt, app

import os
import uuid
from PIL import Image

user = Blueprint('user', __name__)

def check_allowed_file(filename):
    temp = filename.rsplit(".", 1)[1].lower()
    # print(temp)
    if temp in app.config["ALLOWED_FILE"] : return True
    else : return False
    
def get_file_type(filename):
    return filename.rsplit('.', 1)[1].lower()

def process_and_save_image(file, upload_folder):
    if file and check_allowed_file(file.filename):
        filename = secure_filename(str(uuid.uuid4()) + '.' + file.filename.rsplit('.', 1)[1].lower())
        file_path = os.path.join(upload_folder, filename)

        # Save the original file
        file.save(file_path)

        # Open and process the image
        image = Image.open(file_path)
        width, height = image.size

        if width > height:
            left = (width - height) // 2
            right = left + height
            top = 0
            bottom = height
        else:
            top = (height - width) // 2
            bottom = top + width
            left = 0
            right = width

        image = image.crop((left, top, right, bottom))
        image = image.resize((500, 500))

        image.save(file_path)

        return filename

    return None

def delete_image(filename, upload_folder):

    try : 
        os.remove(os.path.join(upload_folder, filename))
    except Exception as e:
        print(e)
        

@user.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("Berhasil logout", "warning")
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

@user.route('/temp', methods=['POST', 'GET'])
def temp():
    if request.method == 'POST':
        if 'profile' not in request.files:
            flash("Profile picture not included.", "danger")
            return redirect(url_for("user.temp"))

        file = request.files['profile']
        
        filename = process_and_save_image(file, app.config['UPLOAD_FOLDER'])
        
        if filename is None:
            flash("File format not accepted.", "danger")
            return redirect(url_for("user.temp"))
        
        flash("Ok success", "success")
        return redirect(url_for('main.view_image', name=filename))
        
    return render_template('main/temp.html')

@user.route('/change_profile_picture', methods=['POST'])
def change_profile_picture():
    if 'profile' not in request.files:
        flash("Profile picture not included.", "danger")
        return redirect(url_for("user.edit_profile"))

    file = request.files['profile']
    
    filename = process_and_save_image(file, app.config['UPLOAD_FOLDER'])   

    if filename is None:
        flash("File format not accepted.", "danger")
        return redirect(url_for("user.edit_profile"))
    
    
    delete_image(current_user.foto_profil, app.config['UPLOAD_FOLDER'])
    user = Pengguna.query.get(current_user.id)
    user.foto_profil = filename
    db.session.commit()
    flash("Profile picture changed successfully.", "success")
    return redirect(url_for('user.edit_profile'))

@user.route('/FAQ')
def FAQ():
    return render_template('user/FAQ.html')