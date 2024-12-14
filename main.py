# This is a sample Python script.
from game_server import GameServer

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from gen_word import SecretWord, State
from wordle import WordleGuess, WordleInit

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    server = GameServer()
    server.add_resource(WordleInit, "/wordle/restart")
    server.add_resource(WordleGuess, "/wordle/guess/<string:word>")
    server.start()
#    game = SecretWord()
#    #print(game.secret)
#    guess = input("? ")
#    bingo = game.guess(guess)
#    print(game.pretty_state())
#    while not bingo:
#        guess = input("? ")
#        bingo = game.guess(guess)
#        print(game.pretty_state())

