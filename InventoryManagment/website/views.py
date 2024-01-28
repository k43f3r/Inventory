from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import select
from website.models import Item
from . import db

from datetime import datetime, date

views = Blueprint("views", __name__)

@views.route('/items')
def home():
    inventory = db.session.execute(db.select(Item)).scalars()
    return render_template("home.html", inventory=inventory)

@views.route("/items/add_item", methods=["GET"])
def add_item():
    return render_template("add_item.html")

@views.route("/items", methods=["POST"])
def create_item():
    equipment_number = request.form.get("equipment_number")
    inventory_number = request.form.get("inventory_number")
    description = request.form.get("description")
    place = request.form.get("place")

    # item = Item.querry.filter_by(equipment_number=equipment_number).first()

    # if item:
    #     flash("Ein Gerät mit dieser Equipment Nummer gibt es bereits!", category='error')
    # elif (equipment_number == None):
    #     flash("Ein Gerät mit dieser Equipment Nummer gibt es bereits!", category='error')
    # elif len(equipment_number < 7):
    #     flash("Die Equipment Nummer muss 7 Stellen umfassen!", category='error')
    # else:

    #     users = db.session.execute(db.select(User).order_by(User.username)).scalars()

    new_item = Item(equipment_number=equipment_number,
                    inventory_number=inventory_number,
                    description=description,
                    place=place)
                                
    db.session.add(new_item)
    db.session.commit()

    flash("Item added!", category="success")

    return redirect(url_for("views.home"))

@views.route("/items/<equipment_number>", methods=["GET"])
def show_item(equipment_number):
    #item = db.session.execute(db.select(Item)).where(Item.equipment_number=="equipment_number").scalars()
    item = Item.query.filter_by(equipment_number=equipment_number).first()
    return render_template("show.html", equipment_number=equipment_number, item=item)

@views.route("/items/<equipment_number>", methods=["POST"])
def update_item(equipment_number):
    #item = db.session.execute(db.select(Item)).where(Item.equipment_number=="equipment_number").scalars()
    item = Item.query.filter_by(equipment_number=equipment_number).first()
    print("Test1")

    new_equipment_number = request.form.get("new_equipment_number")
    new_inventory_number = request.form.get("new_inventory_number")
    new_description = request.form.get("new_description")
    new_place = request.form.get("new_place")

    # new_item = Item(equipment_number=new_equipment_number,
    #                 inventory_number=new_inventory_number,
    #                 description=new_description,
    #                 place=new_place,
    #                 modified_date=new_modified_date)

    item.equipment_number = new_equipment_number
    item.inventory_number = new_inventory_number
    item.description = new_description
    item.place = new_place
    #item.modified_date = datetime
   
    db.session.commit()
    print("db updated")
    return redirect(url_for("views.home"))

# @auth.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         first_name = request.form.get('firstName')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash('Email already exists.', category='error')
#         elif len(email) < 4:
#             flash('Email must be greater than 3 characters.', category='error')
#         elif len(first_name) < 2:
#             flash('First name must be greater than 1 character.', category='error')
#         elif password1 != password2:
#             flash('Passwords don\'t match.', category='error')
#         elif len(password1) < 7:
#             flash('Password must be at least 7 characters.', category='error')
#         else:
#             new_user = User(email=email, first_name=first_name, password=generate_password_hash(
#                 password1, method='sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(new_user, remember=True)
#             flash('Account created!', category='success')
#             return redirect(url_for('views.home'))

#     return render_template("sign_up.html", user=current_user)
        
