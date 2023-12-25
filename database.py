from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import re
from fuzzywuzzy import fuzz
import script_parser as sp

# connection string
uri = "mongodb+srv://brianfedelin:DUnOpHLtmV9Bb699@moviedatabase.ldl5ltv.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['movie_database']
scripts = db['scripts']

def fuzzy_match():
    search_substring = '''Remember the other day when I told
               you about my stand-up comedy. Well,
               I'm doing a set next Thursday and
               I'm inviting a bunch of my friends
               and I was wondering if maybe you
               wanted to come and check it out.'''

    # get all scripts
    matching_scripts = scripts.find()

    # fuzzy match min threshold
    min_fuzzy_score = 80

    # Filter documents with a fuzzy substring match
    for script in matching_scripts:
        # print(script['script_url'])
        print(fuzz.partial_ratio(search_substring,
              sp.parse_script(script['script_url'])))


def get_scripts():
    scripts_collection = scripts.find()
    for script in scripts_collection:
        url = script['script_url']
        scripts.update_one(
            {'_id': script['_id']}, {
                '$set': {'script_text': sp.parse_script(url)}}
        )


def search_script(search_query):
    result = scripts.find({'$text': {'$search': search_query}}, {'score': {'$meta': "textScore"}}
                           ).sort({'score': {'$meta': "textScore"}}).limit(1)

    print(result[0]['title'])


'''create text index for script text in script collection'''
# scripts.create_index([('script_text', 'text')])

search_query = "Slipped? For 30 years your father was in power and did nothing. With you I thought it would be different."

search_script(search_query)
