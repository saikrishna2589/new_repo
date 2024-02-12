
# importing Flask  and render_template
from flask import Flask,render_template

app = Flask(__name__)

# for default page without any parameters, user need to see the home.html

@app.route("/")
def home():
    return render_template("home.html")


#with any api word parameter, return the definition of the word and the word itself as dictionary
@app.route("/api/v1/<word>")
def word_definition(word):
    definition =word.upper()
    result = { "definition":definition,
             "word":word}
    return result


if __name__== "__main__":
    app.run(port=5001)