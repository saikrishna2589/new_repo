
# importing Flask  and render_template
from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)

# for default page without any parameters, user need to see the home.html

@app.route("/")
def home():
    return render_template("home.html")


#with any api word parameter, return the definition of the word and the word itself as dictionary
@app.route("/api/v1/<selected_word>")
def word_definition(selected_word):
    filename="dictionary.csv"
    df= pd.read_csv(filename)

    chosen_row =df.loc[df["word"]==str(selected_word).lower()]
    meaning= chosen_row["definition"].squeeze()
    result = { "word":selected_word,"definition":meaning

               }
    return result


if __name__== "__main__":
    app.run(port=5001)