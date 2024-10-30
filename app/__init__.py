from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

# create instances of alchemy and migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
  # create a new instance of a flask app
  app = Flask(__name__)
  # allow the app to access data from different domains (Cross origin resource sharing)
  CORS(app)

  # connect the app to the database and turn off tracking modification to reduce overhead
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+pg8000://postgres:glxk1306@localhost/task_manager'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  # initialise the alchemy and migrate class with the app and database
  db.init_app(app)
  migrate.init_app(app, db)

  # set a default page that calls the home function 
  @app.route('/')
  def home():
    return "Welcome to the Task Manager API"
  
  # returns an instance of the app when the function create app is called
  return app