from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
  app = Flask(__name__)
  CORS(app)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+pg8000://postgres:glxk1306@localhost/task_manager'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)
  migrate.init_app(app, db)

  @app.route('/')
  def home():
    return "Welcome to the Task Manager API"
  
  return app