from flask_restful import Resource

from src.yellow_pig_game_base.gen_word import SecretWord

class Wordle:
    secret = SecretWord()


class WordleGuess(Resource):

    def get(self, word):
        result = Wordle.secret.guess(word)
        return result

class WordleInit(Resource):

    def get(self):
        Wordle.secret = SecretWord()
        return {
            "initialized" : True
        }


