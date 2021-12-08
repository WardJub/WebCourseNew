from flask import Flask, redirect, url_for

app = Flask (__name__)      #initializing flask server


@app.route('/')        #Putting some content in my homepage / default server entry page.
def home_func():
    return 'Ward Jubran Welcomes You To His Homepage'


@app.route('/home')     #When navigating to /home, redirect to the default homepage ("/") we created earlier
def homeredirect_func():
    return redirect('/')


@app.route('/about')     #Creating an about page
def about_func():
    return 'About Me: My Name Is Ward Jubran & I Love Coding'


#Using The Redirect + URL For: When we navigate To "/aboutme" we will call the function "about_func"
#that we created earlier, and therefore we will be directed to the same content that is in the about page,
@app.route('/aboutme')
def aboutme_func():
    return redirect(url_for('about_func'))



if __name__ == '__main__':  #turning debug on
    app.run(debug=True)