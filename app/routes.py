from flask import Blueprint, request, jsonify
from .models import Task
from . import db

# creates a blueprint to group all the related routes under tasks
tasks_bp = Blueprint('tasks', __name__)

# route for creating new task in database
@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
  # retrieve the json data for new task from user request
  data = request.get_json()

  # creates a new task instance to be addded
  new_task = Task(
    title = data['title'],
    description = data.get('description'),
    due_date = data.get('due_date'),
  )

  db.session.add(new_task)
  db.session.commit()

  # returns the string as a json object to confirm successful creation of new task
  return jsonify({"message" : "Task created successfully"}), 201

# route for getting all tasks from database
@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
  # get all tasks in the data base and store them in variable tasks
  tasks = Task.query.all()
  # convert each task  into a dictionary and store them in a list so that it can be converted into json easily
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
  # return the list of tasks as a json array
  return jsonify(task_list), 200

# route for retrieving a single task with specific id
@tasks_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  # get task with specific id or return 404 error if not task with that id
  task = Task.query.get_or_404(id)
  # convert task into a dictionary so it can be converted into json object easily
  task_data = {
    "id" : task.id,
    "title" : task.title,
    "description" : task.description,
    "completed" : task.completed,
    "due_date" : task.due_date,
    "created_at" : task.created_at
  }
  # returns the task of a specified id as a json object
  return jsonify(task_data), 200

# route for updating the details of a task
@tasks_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  # retrieve task with specific id or return 404 error if no task with that id
  task = Task.query.get_or_404(id)
  # get the fields that needs to be changed from user request
  data = request.get_json()

  # update the fields accoring to user request
  if "title" in data:
    task.title = data['title']
  if 'description' in data:
    task.description = data['description']
  if 'completed' in data:
    task.completed = data['completed']
  if 'due_date' in data:
    task.due_date = data['due_date']

  db.session.commit()

  # return string in the form of json object if task is updated successfully
  return jsonify({"message" : "Task updated successfully"}), 200

# route for deleting a task
@tasks_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
  # retrieve a task of a specific id or return 404 error if no task with that id
  task = Task.query.get_or_404(id)

  db.session.delete(task)
  db.session.commit()

  # return string in the form of a json object if task is deleted successfully
  return jsonify({"message" : "Task deleted successfully"}), 200

