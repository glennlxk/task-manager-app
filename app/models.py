from . import db 
from datetime import datetime

# create task class that inherits from alchemy model class
class Task(db.Model):
  # name the table tasks
  __tablename__ = 'tasks'

  # create the fields for tasks table
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text, nullable=True)
  completed = db.Column(db.Boolean, default=False)
  due_date = db.Column(db.Date, nullable=True)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  # allows any instances of task object to return a string representing it
  def __repr__(self):
    return f"<Task {self.title}>"