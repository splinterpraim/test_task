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
	
	racks = db.session.query(models.Rack,models.Room,models.Customer). \
		select_from(models.Rack). \
		join(models.Room).join(models.Customer).filter(models.Rack.state=="occupied").all()

	racks_json = []
	for ra, r, c in racks:
		racks_json.append({"id" : ra.id,"rack_name":ra.name,"customer_name":c.name,"room name":r.name})
	return racks_json

def query_rooms_array_id():
	rooms = models.Room.query.all()
	customers = models.Customer.query.all()
	rooms_json = []
	for r in rooms:
		
		racks = db.session.query(models.Rack,models.Room,models.Customer). \
		select_from(models.Rack). \
		join(models.Room).join(models.Customer).filter( models.Rack.state=="occupied").all()
		
		rooms_json.append({'id': r.id,'id_customers': list(set([c.id for ra,roo,c in racks if r.id==roo.id]))})
	return rooms_json

def query_rooms_max_rack():
	rooms = models.Room.query.all()
	
	racks_json = []
	for r in rooms:
		racks = db.session.query(models.Rack,models.Room). \
		join(models.Room).filter(models.Room.id==r.id).order_by(models.Rack.size.desc()).all()
		
		if len(racks)<1:
			racks_json.append({'id_room': r.id,'id_rack': None, 'size':None})
		else:
			ra,_  = racks[0]
			racks_json.append({'id_room': r.id,'id_rack': ra.id, 'size':ra.size})
	return racks_json





if __name__ == "__main__":
	app.run( )
