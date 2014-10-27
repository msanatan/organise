from flask import Blueprint, render_template
from organise.models import Todo
from organise import db
from flask import render_template, request, redirect, url_for, flash

todos = Blueprint('todos', __name__, template_folder='/../templates')

@todos.route('/')
def index():
    all_todos = Todo.query.all()
    return render_template('todos.html', todos=all_todos)


@todos.route('/add', methods=['POST'])
def add_todo():
    todo = Todo(request.form['title'], request.form['description'])
    db.session.add(todo)
    db.session.commit()
    flash('New todo was added!')
    return redirect(url_for('todos.index'))


@todos.route('/<int:t_id>')
def show_todo(t_id):
    pass


@todos.route('/<int:t_id>/edit')
def edit_todo(t_id):
    pass


@todos.route('/<int:t_id>/delete', methods=['POST'])
def delete_todo(t_id):
    pass
