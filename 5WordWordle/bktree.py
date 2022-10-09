# lots of help from https://www.geeksforgeeks.org/bk-tree-introduction-implementation/
import nltk
import pybktree

class bkTree():
    def __init__(self, words):
        self.tree = pybktree.BKTree(nltk.edit_distance, words)
        print(self.tree.find("?ater", 1))

