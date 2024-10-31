from flask import Blueprint, request, jsonify
from .models import Task
from . import db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
  data = request.get_json()

  new_task = Task(
    title = data['title'],
    description = data.get('description'),
    due_date = data.get('due_date'),
  )

  db.session.add(new_task)
  db.session.commit()

  return jsonify({"message" : "Task created successfully"}), 201

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
  tasks = Task.query.all()
  task_list = [
    {
      "id" : task.id,
      "title" : task.title,
      "description" : task.description,
      "completed" : task.completed,
      "due_date" : task.due_date,
      "created_at" : task.created_at
    } for task in tasks
  ]
  return jsonify(task_list), 200

@tasks_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  task = Task.query.get_or_404(id)
  task_data = {
    "id" : task.id,
    "title" : task.title,
    "description" : task.description,
    "completed" : task.completed,
    "due_date" : task.due_date,
    "created_at" : task.created_at
  }
  return jsonify(task_data), 200

@tasks_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  task = Task.query.get_or_404(id)
  data = request.get_json()

  if "title" in data:
    task.title = data['title']
  if 'description' in data:
    task.description = data['description']
  if 'completed' in data:
    task.completed = data['completed']
  if 'due_date' in data:
    task.due_date = data['due_date']

  db.session.commit()

  return jsonify({"message" : "Task updated successfully"}), 200

@tasks_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
  task = Task.query.get_or_404(id)

  db.session.delete(task)
  db.session.commit()

  return jsonify({"message" : "Task deleted successfully"}), 200

