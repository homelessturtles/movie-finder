Reel Hunter

Description
Reel Hunter is an application that identifies a movie based on a given audio clip from the movie. It integrates Google cloud's speech to text service and MongoDB's full text search capabilities to search from a database of 250 movie scripts. The database was created by scraping TMBD for 250 popular movies and creating a text index for efficient searching.

How To Use
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages

pip3 install requirements.txt

run app.py to test with sample audio from the movie "Joker"

pass local file into speech_to_text() as an argument in order to test your own movie audio file
