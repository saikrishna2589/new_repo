import requests
from email_automated import send_email

api_key = "4ab757abe0f042728570a4cfce6d64dc"

topic="tesla"


#to the url we are adding '&languge=en' at the end so we only extract english language articles
#in the documnetation on newsapi.com, endpoints, you will find documentation for language and 'en'
url =  "https://newsapi.org/v2/everything"\
       f"?q={topic}&" \
       "sortBy=publishedAt" \
       "&apiKey=4ab757abe0f042728570a4cfce6d64dc"\
       "&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()


print(content["articles"])
# Access the article titles and description for first 20 articles as it is a list of 100 articles
body = ""
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = "Subject: Today's news"\
        +"\n"+ body + article["title"] \
        + "\n" + str(article["description"]) \
        + "\n" + article["url"]+ 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
#this will send email