import random
import json
from datetime import datetime

import requests
from english_words import get_english_words_set
host = 'localhost'
port = 8080
url_path = "/wordle"

def new_word():
    url = f"http://{host}:{port}/{url_path}/restart"
    http_response = requests.get(url)
    return http_response.json()

def guess(word):
    url = f"http://{host}:{port}/{url_path}/guess/{word}"
    http_response = requests.get(url)
    return http_response.json()



######################### SAMPLE CODE #########################
words = list(filter(lambda w : len(w) == 5, get_english_words_set(['gcide'], lower=True)))

if __name__ == '__main__':
    blacklist = set()
    bingo = False
    new_word()
    gloss_matches = [ False, False, False, False, False]
    matches = [ 1, 1, 1, 1, 1 ]
    word = 'XXXXX'
    while not bingo:
        for i in range(0, 5):
            if not gloss_matches[i] and matches[i] == 0:
                words = list(filter(lambda w : w[i] == word[i], words))
                gloss_matches[i] = True
        word = random.choice(words)
        result = guess(word)
        print(f"{word}: {result}")
        matches = result['states']

        bingo = result['result']
        if bingo:
            print("Yeah, " + word)
        else:
            words.remove(word)

######################### SAMPLE CODE #########################