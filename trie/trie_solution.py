# -*- coding:utf-8 -*-
from collections import defaultdict


class TrieNode:
    """
    Trie树的每个节点的结构
    """
    def __init__(self):
        # trie树子树 用数组实现
        self.children = defaultdict(TrieNode)
        # 是否为单词节点
        self.is_word = False


class Trie:

    def __init__(self):
        """
        initialize trie tree
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Trie树插入word
        :param word: 带插入的单词
        :return: None
        """
        cur = self.root
        for letter in word:
            cur = cur.children[letter]
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :param word: str 待查的word
        :return: boolean
        """
        cur = self.root
        for letter in word:
            cur = cur.children.get(letter)
            if cur is None:
                return False
        return cur.is_word

    def starts_with(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for letter in prefix:
            cur = cur.children.get(letter)
            if cur is None:
                return False
        return True

    def get_start_words(self, prefix):
        """
        Returns words started with prefix
        :param prefix: 前缀字符
        :return: words -> list
        """
        def get_key(pre, pre_node):
            """

            :param pre:
            :param pre_node:
            :return:
            """
            word_list = []
            if pre_node.is_word:
                word_list.append(pre)

            for x in pre_node.children.keys():
                word_list.extend(get_key(pre + str(x), pre_node.children.get(x)))
            return word_list

        words = []
        if not self.starts_with(prefix):
            return words
        if self.search(prefix):
            words.append(prefix)
            return words

        node = self.root
        for char in prefix:
            node = node.children.get(char)
        return get_key(prefix, node)


if __name__ == "__main__":
    obj = Trie()
    obj.insert("china")
    obj.insert("chine")
    obj.insert("chian")
    obj.insert("cheer")
    obj.insert("japan")
    obj.insert("america")
    obj.insert("american")
    obj.insert("hello")
    obj.insert("helo")
    obj.insert("heihei")
    print(obj.search("chine"))
    print(obj.starts_with("jap"))
    print(obj.get_start_words("he"))
    print(obj.get_start_words(""))
