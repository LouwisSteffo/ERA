from flask import Blueprint, render_template, url_for, request, flash, redirect , jsonify
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from webdata.models import Pengguna , Kupon ,Redeem
from webdata import db , bcrypt


redeem = Blueprint('redeem', __name__)

@redeem.route('/')
@login_required
def index():
    return render_template('main/index.html')

@redeem.route('/redeem_poin')
@login_required
def redeem_poin():
    allKupon = Kupon.query.all()
    # flash("This works", "danger")

    return render_template('redeem/redeem.html' , allKupon = allKupon)

@redeem.route('/tukar_poin', methods=['POST'])
@login_required
def tukar_poin():
    # flash('Working Nicely', 'success')
    # Get user ID
    user_id = current_user.id

    # Get coupon ID from the request
    if request.is_json:
        data = request.json
        id_kupon = data.get('id_kupon')
    else:
        return jsonify({'error': 'Request must be in JSON format'}), 400
    
    

    # Check if the coupon ID is valid
    kupon = Kupon.query.get(id_kupon)
    if kupon is None:
        # flash('Invalid coupon ID', 'error')
        return jsonify({'message' : "Invalid coupon ID"}), 400
    

    # Retrieve the user from the database
    pengguna = Pengguna.query.get(user_id)
    if pengguna is None:
        # flash('User not found', 'error')
        return jsonify({'message' : "Failed"}, 401)
    # Check if the user has enough points to redeem the coupon
    if pengguna.poin < kupon.harga_kupon:
        # flash('Insufficient points', 'error')
        return jsonify({'message' : "Insufficient points."}), 400
    
    # Decrease the user's points
    pengguna.poin -= kupon.harga_kupon
    
    kupon.jumlah_kupon -=1

    # Save the changes to the database
    db.session.commit()
    
    new_redeem = Redeem(id_pengguna = user_id , id_kupon = id_kupon)
    
    db.session.add(new_redeem)
    db.session.commit()
    

    # Display a success message
    # flash('Coupon redeemed successfully!', 'success')

    # Redirect to the redeem page
    return jsonify({'message' : "Coupon redeemed succesfully!"}), 200


    


    
    #NOTE YANG HARUS DILAKUKAN
    #kita perlu ambil id kupon ke berapa, jadi nanti akan nguranginnya ke id kuponnya yang dituju
    
    #Di bagian html nanti kalau jumlah kuponnya di database = 0  maka jangan dikeluarin kuponnya.
    
    
    # return render_template('redeem/redeem.html', poin_user = poin_user)