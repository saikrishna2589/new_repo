
#request library will get the page sourcecode and stores in a string (when you click Viewpagesource on website,
#you can see it.
import requests

# selectorlib will exact only particular info from the source code retrieved.
import selectorlib
URL="https://programmer100.pythonanywhere.com/tours/"


#sraping , #arsing, #storing in textfile or sql database-->steps in this app

def scrape(url):
    """Scrape the page source from URL"""
    response=requests.get(url)
    source_text=response.text
    return source_text

#extracting page source code
def extract(source_text):
    #calling method
    extractor=selectorlib.Extractor.from_yaml_file("extract.yaml")
    #the below will return dictionary, so we pull the key 'tours' to get its value #displaytimer,which is id of the tag
    value=extractor.extract(source_text)["tours"]
    return value

def send_email():
    print("Email was sent")


#storing extracted event value in text file and appended the new value everytime we run the function.
def store(extracted):
    with open("data.txt","a") as file:
        file.write(extracted+"\n")
def read(extracted):
    with open("data.txt","r") as file:
        return  file.read()


if __name__=="__main__":
    scraped=scrape(URL)
    extracted=extract(scraped)
    print(extracted)

    content=read(extracted)
    if extracted!="No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email()

#extract only info we need which is in h1 tag, we use selectorlib


