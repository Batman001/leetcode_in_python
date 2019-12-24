# -*- coding:utf-8 -*-
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)

        self.is_word = False


class TrieSolution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for letter in word:

            cur = cur.children[letter]
        cur.is_word = True

    def search(self, word):
        cur = self.root
        for letter in word:
            cur = cur.children[letter]
            if cur is None:
                return False
        return cur.is_word

    def starts_with(self, prefix):
        cur = self.root
        for letter in prefix:
            cur = cur.children[letter]

            if cur is None:
                return False
        return True


