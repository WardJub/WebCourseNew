from flask import Flask, redirect, url_for, render_template

app = Flask (__name__)


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
    return render_template('assignment8.html', tvshows=('Mr. Robot', 'Vikings', 'Peaky Blinders', 'Rick And Morty', 'Sherlock'))

# Now that I created the assignment 8 html, I will continue my work on the html file assignment8.html


if __name__ == '__main__':
    app.run(debug=True)     #this is how we intialize the server.
