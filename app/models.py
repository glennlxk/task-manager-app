from . import db 
from datetime import datetime

class Task(db.Model):
  __tablename__ = 'tasks'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(500))
  status = db.Column(db.String(20), default='to-do')
  due_date = db.Column(db.Date, nullable=True)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return f"<Task {self.title}>"