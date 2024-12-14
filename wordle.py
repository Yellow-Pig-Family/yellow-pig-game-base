from flask_restful import Resource

from gen_word import SecretWord

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
            "secret" : Wordle.secret.secret,
            "initialized" : True
        }


