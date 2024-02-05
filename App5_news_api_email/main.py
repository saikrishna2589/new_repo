
#importing requests library to read apis for webpages
import requests

#go to newsapi.org ,login and get the api_key
api_key="4ab757abe0f042728570a4cfce6d64dc"
url = ("https://newsapi.org/v2/everything?q=bitcoin&from=2024-01-05&"
       "sortBy=publishedAt&apiKey"
       "=4ab757abe0f042728570a4cfce6d64dc")

#this is a function that gets url. requests.get function creates a request object type.
request = requests.get(url)

#this method .txt prints out the content in string format. so type of content is string
content_text=request.text

#however if you want data in more structuted way such as dictionary , we use .json method on request object
content_dict=request.json()
'print(content_dict["articles"])'
'print(len(content_dict["articles"]))'

#content_dict is a dictionary and has articles as a key. the values are again a list of 100 items.
# and each item has key value pairs
"""for article in content_dict["articles"]:'
       print(article["description"])"""

#getting each value in the list of 100 articles key by accessing the title key within each list
for article in content_dict["articles"]:
       print(article["title"])


