from . import db

class Item(db.Model):
    equipment_number = db.Column(db.Integer, unique=True, primary_key=True)
    inventory_number = db.Column(db.Integer, unique=True)
    description = db.Column(db.String(150))
    place = db.Column(db.String(150))
    creation_date = db.Column(db.DateTime, server_default=db.func.now())
    modified_date = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

class History(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    history = db.Column(db.String(2000))
    item_equipment_number = db.Column(db.Integer, db.ForeignKey("item.equipment_number"), nullable=False)
