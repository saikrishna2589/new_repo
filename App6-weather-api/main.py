
# webframework FLask would manage multiple html pages.
#it is responsbile for ensuring multiple webpages interact correctly
from flask import Flask,render_template


import pandas as pd
#Flask has website objects to represent websites similar to string,list object to represent series of data, etc

#only if the __name__=="m__main__" , as in we are running the program where the syynax is written, we run the file.
#if we import this function to another pythin file and run it, it wont run t
app = Flask(__name__)

#Now we need to connect html pages with this website object.
# whenever user clicks on home, "HTMLtutorial.html" page comes up.
# this HTMLtutorial.html page should be in a special folder within root directory called 'templates'
#so Flask will look for HTML doucments by defual in that 'templates' folder

# the url will be connected to HTML documenti.e when user visits the URL, the home() function is called

#The '@" symbol in @app.route(\"home) means '@'is a decorator and it connects the route method to the function home()


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/api/v1/<station>/<date>")
def station_date(station,date):

    station=str(station).zfill(6)
    filename ="data_small/TG_STAID"+ station+".txt"
    df=pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])

    chosen_row_and_date=df.loc[df["    DATE"]==date]
    temperature=chosen_row_and_date['   TG'].squeeze()/10
    return {"Station": station.lstrip('0'),
            "date": date,
            "temperate": temperature}



#debug argument true allows to see erros on the webpage
if __name__=="__main__":
    app.run()

"""if __name__=="__main__":
    app.run('debug=True',port=)"""
"""if we are running multiple Flask apps, (here it is just one but incase), we can specify the default port.
if not, port 5000 is the default and will be occupied by the first flask app.

if __name__=="__main__":
    app.run(port=5001) 
    """

# so basically we have a python file,in this case 'main.py' and it is managing multiple html files interactions through
#FLASK web framework