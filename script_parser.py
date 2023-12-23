from bs4 import BeautifulSoup
import requests

'''
    later check if movie already in database
'''

def remove_newlines(string):
    return string.replace('\n', '').replace('\r', '')

def parse_script(scripturl): 
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    result = requests.get(scripturl, headers=header)

    soup = BeautifulSoup(result.text, "html.parser")

    script = str(soup.find(class_='scrtext'))
    script = script.replace("</b>", " ")
    script = script.replace("<b>", " ")
    script = remove_newlines(script)

    return script

with open('joker_script.txt', 'w') as file:
    file.write(parse_script('https://imsdb.com/scripts/Joker.html'))