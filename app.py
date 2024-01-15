import database as db

reelhunter = db
search_query = reelhunter.speech_to_text('audio/joker_monologue_Master.wav')

reelhunter.search_script(search_query)