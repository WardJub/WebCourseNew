from flask import Blueprint, render_template, request, redirect
from interact_with_database import interact_db

# about blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')


# Routes
@assignment10.route('/assignment10')
def assignment10_func():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result) # showing the user list


@assignment10.route('/insert_user' , methods=['POST'])  # post we want to hide password from URL.
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    query = "INSERT INTO users (name,email,password) VALUES ('%s','%s','%s')" % (name, email, password)
    inserted = interact_db(query=query, query_type='commit')  # inserted variable will help us display the message.
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', inserted=inserted, users=query_result)  # the inserted boolean will help display message.


@assignment10.route('/update_user' , methods=['POST'])
def update_user_func():
    id = request.form['id']
    email = request.form['email']
    query = "UPDATE users SET email='%s' WHERE id='%s' " % (email, id)
    updated = interact_db(query=query, query_type='commit')  # inserted variable will help us display the message.
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', updated=updated, users=query_result)  # the updated boolean will help display message.


@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    id = request.form['id']
    query = "DELETE FROM users WHERE id='%s' " % (id)
    deleted = interact_db(query=query, query_type='commit')  # inserted variable will help us display the message.
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', deleted=deleted, users=query_result)  # the updated boolean will help display message.
