import random
import json

import requests
from english_words import get_english_words_set
host = 'localhost'
port = 8080
url_path = "/wordle/"

def new_word():
    url = f"http://{host}:{port}/{url_path}/restart"
    http_response = requests.get(url)
    return json.loads(http_response.content)

def guess(word):
    url = f"http://{host}:{port}/{url_path}/guess/{word}"
    http_response = requests.get(url)
    return json.loads(http_response.content)

words = list(filter(lambda w : len(w) == 5, get_english_words_set(['gcide'], lower=True)))

if __name__ == '__main__':
    while True:
        bingo = False
        new_word()
        while not bingo:
            word = random.choice(words)
            result = guess(word)
            print(f"{word}: {result}")
            bingo = result['result']
            if bingo:
                print("Yeah, " + word)