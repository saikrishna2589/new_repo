
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


stations=pd.read_csv("data_small/stations.txt",skiprows=17,delimiter=',')
stations.columns=stations.columns.str.strip()
stations_main=stations[["STAID","STANAME" ]]


# in return, you want to return data variable on the website. but this page is connected to home.html page
#so in home.html page, use special double curly bracket <p{{data}}</p to reflect the variable info on website
#however as the html method ofthe dataframe variable data= stations_main.to_html()needs to be rendered properly on website, you tell flask a
#command . so you give< p{{data|safe}}</p . this '|safe' will render the html format correctly
print(stations_main)
@app.route("/")
def home():
    return render_template("home.html",data=stations_main.to_html())



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


@app.route("/api/v1/<station_id>")
def station_id(station_id):
    station_id=str(station_id).zfill(6)
    filename1=pd.read_csv("data_small/TG_STAID"+station_id+".txt",skiprows=20,parse_dates=["    DATE"])
    filename2=filename1[["STAID"," SOUID","    DATE"]]
    return render_template("home1.html",chosen_station=filename2.to_html())
  # to show result on website in dictionary method. here we are not rendering any template but showing result directly.
    #result=filename2.to_dict(orient="records")
    #return result


@app.route("/api/v1/yearly/<station_id>/<year>")
def station_year(station_id,year):
    station_id=str(station_id).zfill(6)
    file=pd.read_csv("data_small/TG_STAID"+station_id+".txt",skiprows=20,parse_dates=["    DATE"])
    #chaning date column date date type to string data type so as to apply string methods on it
    file['    DATE'] = file['    DATE'].astype(str)
    df=file.loc[file['    DATE'].str.startswith(str(year))]
    return render_template("station_year.html",data1=df.to_html())
    #returning dictionary instead
    #result= df.to_dict(orient="records")
    #return result









#debug argument true allows to see erros on the webpage
if __name__=="__main__":
    app.run(port=5002)

"""if __name__=="__main__":
    app.run('debug=True',port=)"""
"""if we are running multiple Flask apps, (here it is just one but incase), we can specify the default port.
if not, port 5000 is the default and will be occupied by the first flask app.

if __name__=="__main__":
    app.run(port=5001) 
    """

# so basically we have a python file,in this case 'main.py' and it is managing multiple html files interactions through
#FLASK web framework