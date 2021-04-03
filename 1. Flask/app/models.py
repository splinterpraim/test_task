from app import db

class Room(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)

	def __repr__(self):
		return f'Room {self.id}'


class Rack(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	size = db.Column(db.Integer)
	state = db.Column(db.Text)
	customer = db.Column(db.Integer, db.ForeignKey('customer.id'))
	room_id = db.Column(db.Integer, db.ForeignKey('room.id'))

	def __repr__(self):
		return f'Rack {self.id}'

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)

	def __repr__(self):
		return f'Customer {self.id}'
	
#