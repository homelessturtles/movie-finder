from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import re
from fuzzywuzzy import fuzz
import script_parser as sp

#connection string
uri = "mongodb+srv://brianfedelin:DUnOpHLtmV9Bb699@moviedatabase.ldl5ltv.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

def download_scripts():
    db = client['movie_database']
    scripts = db['scripts'].find()

    for script in scripts:
        url = script['script_url']
        name = script['title']
        with open(f'{name}.txt', 'w') as file:
            file.write(sp.parse_script(url))


def fuzzy_match():
    db = client['movie_database']
    scripts = db['scripts']

    search_substring = 'Im doing a set next Thursday'

    # get all scripts
    matching_scripts = scripts.find()

    # fuzzy match min threshold
    min_fuzzy_score = 80

    # Filter documents with a fuzzy substring match
    filtered_scripts = [
        script for script in matching_scripts
        if fuzz.partial_ratio(search_substring, script.get('script_text', '')) >= min_fuzzy_score
    ]

    # Print the matching documents
    for script in filtered_scripts:
        print(script['name'])

download_scripts()