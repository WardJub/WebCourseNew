from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, jsonify, request
from interact_with_database import interact_db
import requests

app = Flask(__name__)
app.secret_key = '123'
app.config.from_pyfile('settings.py')


# Creating the default route "/" and connecting it to the CV HTML page that i created in previous homeworks: (added
# it to templates)
@app.route('/')
def default_func():
    return render_template('CVgrid.html')


# Redirecting to the same page when we navigate to the route "/home": (using URL FOR)
@app.route('/home')
def home_func():
    return redirect(url_for('default_func'))


# Now I will go to the html file 'CVgrid' and connect it to the css file that we copied into 'static' folder.
# I also updated the image source (to static/images path that we created)
# I linked the CV grid To another html file that I created in a previous homework in order to add a little bit more
# The file is called forms.html and it's connected also to a css, I updated the css path to static/css/relevantCSSfile
# I linked them by using a-href, and I will create the root now and link it to the href also.

@app.route('/contactme')
def contactme_func():
    return render_template('forms.html')


# I added a link a-href to the homepage "CLICK HERE TO VISIT ASSIGNMENT 8",Now I will link the route to assignment8.html

@app.route("/assignment8")
def assignment8_func():
    return render_template('assignment8.html',
                           tvshows=('Mr. Robot', 'Vikings', 'Peaky Blinders', 'Rick And Morty', 'Sherlock'))


# Now that I created the assignment 8 html, I will continue my work on the html file assignment8.html


# ********************************************* Assignment 9 ****************************************************

# Created an HTML template called Assignment 9.


# Creating Assignment 9 route:
@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    if request.method == 'GET':  # if we enter with get method
        if 'name' in request.args:
            name = request.args['name']  # get the name from the form input
            session['name'] = name
            if name == '':  # if the user did an empty search
                return render_template('assignment9.html',
                                       users={'user1': {'name': 'ward', 'email': 'ward@post.com'},
                                              'user2': {'name': 'alex', 'email': 'Alex@gmail.com'},
                                              'user3': {'name': 'yossi', 'email': 'Yossi@yo.com'},
                                              'user4': {'name': 'jimmy', 'email': 'JimJim@jimmy.com'},
                                              'user5': {'name': 'moshe', 'email': 'moshimosh@moshi.co.il'}})

            else:  # if the user searched for a certain name
                return render_template('assignment9.html', name=name,
                                       users={'user1': {'name': 'ward', 'email': 'ward@post.com'},
                                              'user2': {'name': 'alex', 'email': 'Alex@gmail.com'},
                                              'user3': {'name': 'yossi', 'email': 'Yossi@yo.com'},
                                              'user4': {'name': 'jimmy', 'email': 'JimJim@jimmy.com'},
                                              'user5': {'name': 'moshe', 'email': 'moshimosh@moshi.co.il'}})

        else:  # if the user didn't do anything (just entered the page):
            return render_template('assignment9.html')

    if request.method == 'POST':  # if the user used the Post form (registration)
        name = request.form['nickname']  ##form is for form post parameters, args is for GET method parameters
        password = request.form['password']
        # TODO DB CHECK IF USER INFO EXISTS
        session['username'] = name
        return render_template('assignment9.html')
    return render_template('assignment9.html')


@app.route('/logout')  # create logout
def logout_func():
    session['username'] = ''
    return redirect(url_for('assignment9_func'))


# ********************************************* Assignment 10 ****************************************************
# Creating a blueprint for assignment 10:
# Added pages + assignment 10 directories, added settings.py and used it above

from pages.assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)


# ********************************************* Assignment 11 ****************************************************
@app.route('/assignment11/users')
def assignment11_users_func():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return jsonify(query_result)  # returns all users with all fields as json
                                  # Ordered in the proper way.


@app.route('/assignment11/outer_source')
def assignment11_outer_source_func():
    # return render_template('assignment11.html')
    if "number" in request.args:
        usertosearch = int(request.args['number'])
        userfound = get_user(usertosearch)
        return render_template('assignment11.html', userfound=userfound)
    return render_template('assignment11.html')


def get_user(num):
    # usertoshow = []
    num = str(num)
    res = requests.get(url=f'https://reqres.in/api/users/{num}')
    res = res.json()
    # usertoshow.append(res)
    return res


# ********************************************* Assignment 12 ****************************************************


@app.route('/assignment12/restapi_users', defaults={'user_id': 1})  # setting a default user in case no id is provided
@app.route('/assignment12/restapi_users/<int:user_id>', methods=['GET', 'POST'])
def get_user_json(user_id):
    query = "select * from users where id=%s" % user_id
    query_result = interact_db(query=query,query_type='fetch')
    if len(query_result) == 0:
        return_dict = {'status': 'failed', 'message': 'user not found'}  # show error message if user is not found
    else:                                                                # if user is found, return it in json format:
        return_dict = {'status': 'success', 'name': query_result[0].name, 'email': query_result[0].email}
    return jsonify(return_dict)





if __name__ == '__main__':
    app.run(debug=True)  # this is how we intialize the server.
