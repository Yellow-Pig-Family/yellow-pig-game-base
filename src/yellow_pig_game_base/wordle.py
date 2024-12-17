from flask_restful import Resource
from flask import request
from datetime import datetime, timedelta

from src.yellow_pig_game_base.gen_word import SecretWord

class Wordle:
    context = {}
    statistic = {}

def new_word():
    print('Generate new word')
    secret = SecretWord()
    return {
        'secret' : secret,
        'count' : 0,
        'last-guess' : None,
        'last-result' : None,
        #'secret-word' : secret.secret,
        'start-time' : datetime.now(),
        'duration' : None
    }

def get_or_init():
    if request.remote_addr not in Wordle.context:
        Wordle.context[request.remote_addr] = []
    return Wordle.context[request.remote_addr]

class WordleGuess(Resource):

    def get(self, word):
        records = get_or_init()
        if len(records) == 0:
            records.append(new_word())
        records[-1]['count'] += 1
        records[-1]['last-guess'] = word
        result = records[-1]['secret'].guess(word)
        records[-1]['last-result'] = result
        records[-1]['duration'] = datetime.now() - records[-1]['start-time']
        result['count'] = records[-1]['count']
        result['duration'] = records[-1]['duration'].total_seconds()
        return result

class WordleInit(Resource):

    def get(self):
        records = get_or_init()
        records.append(new_word())
        records[-1]['duration'] = datetime.now() - records[-1]['start-time']
        print(records)
        return {
            "initialized" : True
        }


