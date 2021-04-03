from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app,db)
import models

@app.route('/')
def index():
	return "Hello world"

if __name__ == "__main__":
	app.run( )
