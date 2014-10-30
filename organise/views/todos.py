from flask import Blueprint, render_template, request, redirect, url_for, flash
from organise.models import Todo
from organise import db

todos = Blueprint('todos', __name__, template_folder='/../templates')

@todos.route('/')
def index():
    all_todos = Todo.query.order_by(Todo.id.desc()).all()
    return render_template('todos.html', all_todos=all_todos)


@todos.route('/add', methods=['POST'])
def add_todo():
    todo = Todo(request.form['title'], request.form['description'])
    db.session.add(todo)
    db.session.commit()
    flash('New todo was added')
    return redirect(url_for('todos.index'))


@todos.route('/todo/<int:t_id>')
def show_todo(t_id):
    todo = Todo.query.filter_by(id=t_id).first()
    return render_template('todo.html', todo=todo)


@todos.route('/todo/<int:t_id>/edit', methods=['POST'])
def edit_todo(t_id):
    changed_title = request.form['title']
    changed_description = request.form['description']
    todo = Todo.query.filter_by(id=t_id).first()
    todo.title = changed_title
    todo.description = changed_description
    db.session.commit()
    flash('All changes were saved')
    return redirect(url_for('todos.index'))


@todos.route('/todo/<int:t_id>/delete', methods=['POST'])
def delete_todo(t_id):
    todo = Todo.query.filter_by(id=t_id).first()
    db.session.delete(todo)
    db.session.commit()
    flash('Todo successfully deleted')
    return redirect(url_for('todos.index'))
