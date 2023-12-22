import requests
import re
import urllib3

from bs4 import BeautifulSoup

#test code to parse throguh script given movie title

movies = ["Joker", "Black Panther", "A Prayer Before Dawn"]

quote = '''(continuing without taking
                    a breath)
               Remember the other day when I told
               you about my stand-up comedy. Well,
               I'm doing a set next Thursday and
               I'm inviting a bunch of my friends
               and I was wondering if maybe you
               wanted to come and check it out.'''

def remove_newlines(string):
    return string.replace('\n', '').replace('\r', '')



for movieName in movies:
    movieName = movieName.replace(" ", "-")
    url = "https://imsdb.com/scripts/title.html"
    url = url.replace("title", movieName)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
  
    result = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(result.text, "lxml")
    
    script = str(soup.find(class_ = "scrtext"))
    script = script.replace("</b>", " ")
    script = script.replace("<b>", " ")
    script = remove_newlines(script)
    haystack = re.sub('[\W_]+', ' ', script)

    needle = remove_newlines(quote)
    needle = re.sub('[\W_]+', ' ', needle)

    fp = haystack.find(needle)
    if fp != -1:
        print(f"found in {movieName}")
    else:
        print("not found")


'''
machine learning facial recognition

transcribing the clip on what they said

parsing actors from machine learning

getting common movies from actors

parse through script 
'''
