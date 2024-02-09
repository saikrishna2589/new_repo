
url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Siam_lilacpoint.jpg/221px-Siam_lilacpoint.jpg"


import requests

response = requests.get(url)

#for loading text data, we use response.text but this is an image,so we need to use response.content
print(response.content)


#we need to write the image bytes code that was printed to a file .image files are written in 'wb' write binary mode.
#as oppossed to text in 'w' write mode

with open("image.jpg", "wb") as file:
    file.write(response.content)


