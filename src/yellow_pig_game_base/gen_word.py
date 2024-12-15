import random

from english_words import get_english_words_set
from enum import Enum


class State(int, Enum):
    Invalid = 3
    Missed = 1
    Exists = 2
    Hit = 0


class SecretWord:
    max_length = 5
    states = [State.Missed, State.Missed, State.Missed, State.Missed, State.Missed]

    def __init__(self):

        self.word_list = list(get_english_words_set(['gcide'], lower=True))
        w = random.choice(self.word_list)
        while len(w) != self.max_length:
            w = random.choice(self.word_list)
        self.secret = w
        print()

    def guess(self, word):
        if (len(word) != self.max_length):
            return {
                "result": False,
                "reason": "Invalid Length"
            }

        if word not in self.word_list:
            return {
                "result": False,
                "reason": "Not a word"
            }

        for i in range(0, self.max_length):

            if word[i] == self.secret[i]:
                self.states[i] = State.Hit
            elif word[i] in self.secret:
                self.states[i] = State.Exists
            else:
                self.states[i] = State.Missed
        result = 0
        for state in self.states:
            result += state.value
        return {
            "result": result == 0,
            "reason": "",
            "states": self.states
        }

    def pretty_state(self):
        result = ""
        for state in self.states:
            match state:
                case State.Missed:
                    result += "[X]"
                case State.Exists:
                    result += "[?]"
                case State.Hit:
                    result += "[O]"
                case State.Invalid:
                    result += "[@]"

        return result
