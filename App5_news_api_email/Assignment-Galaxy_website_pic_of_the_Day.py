
import streamlit as st
import requests

api_key="ghqvaxwFCCfvx30loJd0IcxaTL5i1hJoLqDwjoPk"
url = "https://api.nasa.gov/planetary/apod?"\
       f"api_key={api_key}"


#Get the request data as a dictionary
response = requests.get(url)
data=response.json()



#Extract the image title, url and explanation
title=data["title"]
image_url=data["url"]
explanation=data["explanation"]

#Download the image
#write the response of the url content into the file
image_filepath="Img.png"
response2=requests.get(image_url)
with open (image_filepath,"wb") as file:
    file.write(response2.content)


#into streamlit
st.title(title)
st.image(image_url)
st.write(explanation)
