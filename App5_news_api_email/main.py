import requests
from email_automated import send_email

api_key = "4ab757abe0f042728570a4cfce6d64dc"
url = "https://newsapi.org/v2/everything?q=bitcoin&" \
      "sortBy=publishedAt&apiKey=" \
      "4ab757abe0f042728570a4cfce6d64dc"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)