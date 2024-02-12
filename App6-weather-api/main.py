
# webframework FLask would manage multiple html pages.
#it is responsbile for ensuring multiple webpages interact correctly
from flask import Flask,render_template

#Flask has website objects to represent websites similar to string,list object to represent series of data, etc
app = Flask("Website")

#Now we need to connect html pages with this website object.
# whenever user clicks on home, "HTMLtutorial.html" page comes up.
# this HTMLtutorial.html page should be in a special folder within root directory called 'templates'
#so Flask will look for HTML doucments by defual in that 'templates' folder

# the url will be connected to HTML documenti.e when user visits the URL, the home() function is called

#The '@" symbol in @app.route(\"home) means '@'is a decorator and it connects the route method to the function home()


@app.route("/home")
def home():
    return render_template("HTMLtutorial.html")


@app.route("/about/")
def about():
    return render_template("about.html")



#debug argument true allows to see erros on the webpage
app.run()


# so basically we have a python file,in this case 'main.py' and it is managing multiple html files interactions through
#FLASK web framework