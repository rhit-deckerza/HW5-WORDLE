from bktree import bkTree
from wordle import Wordle
from words import Words
import random

words = Words()
wordle = Wordle(words.words, random)
data = [0] * 417
wordle.guess("crane", data)
