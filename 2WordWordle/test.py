from wordle import Wordle
from words import Words
import random
words = Words()
wordle = Wordle(words.words, random)
data = [0] * 131
wordle.guess("po", data)