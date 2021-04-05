from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import json

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app,db)
import models

@app.route('/')
def index():
	return "Hello world"


@app.route('/a')
def a():

	rooms =  models.Room.query.all()
	print(rooms[0].racks)
	return "Good"
@app.route('/all')
def all():
	
	final = json.dumps(dict([
		query_room_all(),
		query_customer_all(),
		query_rack_all()
		]),ensure_ascii = False)

	print(final)	
	return final

@app.route('/racks_occupied')
def racks_occupied():
	return json.dumps({"Racks_occupied":query_racks_occupied()},ensure_ascii = False)

@app.route('/rooms_array_id')
def rooms_array_id():
	return json.dumps({"Rooms_array":query_rooms_array_id()},ensure_ascii = False)

@app.route('/rooms_max_rack')
def rooms_max_rack():
	return json.dumps({"Max_Rack":query_rooms_max_rack()},ensure_ascii = False)




# REQUESTS
def query_room_all():
	rooms = models.Room.query.all()
	rooms_json = []
	for r in rooms:
		rooms_json.append({"id" : r.id,"name":r.name})
	return ("Room",rooms_json)

def query_customer_all():
	customers = models.Customer.query.all()
	customers_json = []
	for c in customers:
		customers_json.append({"id" : c.id,"name":c.name})
	return ("Customer",customers_json)

def query_rack_all():
	racks = models.Rack.query.all()
	racks_json = []
	for ra in racks:
		racks_json.append({"id" : ra.id,"name":ra.name,"size":ra.size,"state":ra.state,"customer":ra.customer,"room_id":ra.room_id})
	return ("Rack",racks_json)

def query_racks_occupied():
	racks = models.Rack.query.filter(models.Rack.state == 'occupied').all()
	racks_json = []
	for ra in racks:
		racks_json.append({"id" : ra.id,"rack_name":ra.name,"customer_name":ra.cust.name,"room name":ra.room.name})
	return racks_json

def query_rooms_array_id():
	racks = models.Rack.query.filter(models.Rack.state == 'occupied').all()
	rooms_json = []
	for ra in racks:
		r = ra.room
		rooms_json.append({'id': r.id,'id_customers': [c.id for c in r.customer]})

	racks = models.Room.query.join(models.Rack,Room.id,Rack.room_id).


	# rooms = db.session.query(models.Room).all()
	# rooms_json = []
	# for r in rooms:
	# 	rooms_json.append({'id': r.id,'id_customers': list(set([x.customer for x in r.racks]))})
	return rooms_json

def query_rooms_max_rack():
	rooms = db.session.query(models.Room.id, models.Rack.id, db.func.max(models.Rack.size)). \
			outerjoin(models.Rack, models.Room.id == models.Rack.room_id).group_by(models.Room.id).all()

	racks_json = []
	for ro,ra, ra_size in rooms:
		racks_json.append({'id_room': ro,'id_rack': ra, 'size':ra_size})
	return racks_json





if __name__ == "__main__":
	app.run( )
