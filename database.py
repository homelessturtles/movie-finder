from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import script_parser as sp
from speechtext import speech_to_text

'''
todo

find popular movies list
use movie list to populate database with movies & scripts
test with a lot of movie scripts in db
'''

# connection string
uri = "mongodb+srv://brianfedelin:DUnOpHLtmV9Bb699@moviedatabase.ldl5ltv.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['movie_database']
scripts = db['scripts']


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

search_query = speech_to_text('audio/joker_monologue_Master.wav')

search_script(search_query)

