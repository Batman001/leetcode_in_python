from collections import defaultdict


class TrieNode:
    def __init__(self):
        # 每一个Trie树的节点使用默认字典实现
        self.children = defaultdict(TrieNode)
        # 当前截止到本节点是否为word
        self.is_word = False


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Trie树中插入一个word
        :param word:
        :return:
        """
        cur_node = self.root
        for letter in word:
            cur_node = cur_node.children[letter]
        cur_node.is_word = True

    def search(self, word):
        """
        查询Trie树中是否存在该word
        :param word: 待查询word
        :return:
        """
        cur_node = self.root
        for letter in word:
            cur_node = cur_node.children[letter]
            if cur_node is None:
                return False
        return cur_node.is_word

    def starts_with_prefix(self, prefix):
        """
        查询Trie树中是否存在该前缀
        :param prefix:
        :return:
        """
        cur_node = self.root
        for letter in prefix:
            cur_node = cur_node.children[letter]
            if cur_node is None:
                return False
        return True

    def get_start_words(self, prefix):
        """
        查询Trie树中全部以prefix开头的words
        :param prefix: 前缀为prefix
        :return:
        """
        words = []

        if not self.starts_with_prefix(prefix):
            return words

        if self.search(prefix):
            words.append(prefix)

        # 获取到前缀树最后一个子节点
        cur_node = self.root
        for letter in prefix:
            cur_node = cur_node.children[letter]

        return self.get_key_words(prefix, cur_node)

    def get_key_words(self, pre, pre_node):
        """
        递归实现 获取以pre为前缀 以pre_node为TrieNode节点的words_list
        :param pre: 前缀
        :param pre_node: 前缀的最后一个TrieNode节点
        :return: 添加前缀的words_list
        """
        words_list = []
        if pre_node.is_word:
            words_list.append(pre)

        for x in pre_node.children.keys():
            words_list.extend(self.get_key_words(pre + str(x), pre_node.children.get(x)))
        return words_list


if __name__ == "__main__":
    obj = TrieTree()

    obj.insert("chine")
    obj.insert("chin")
    obj.insert("chian")
    obj.insert("cheer")
    obj.insert("japan")
    obj.insert("america")
    obj.insert("american")
    obj.insert("hello")
    obj.insert("helo")
    obj.insert("heihei")
    obj.insert("he")
    print(obj.search("chin"))
    print(obj.starts_with_prefix("jape"))
    print(obj.get_start_words("chin"))
