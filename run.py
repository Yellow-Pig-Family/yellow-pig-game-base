from src.yellow_pig_game_base.game_server import GameServer
from yellow_pig_game_base.wordle import WordleInit, WordleGuess

if __name__ == '__main__':
    server = GameServer()
    server.add_resource(WordleInit, "/wordle/restart")
    server.add_resource(WordleGuess, "/wordle/guess/<string:word>")
    server.start()
