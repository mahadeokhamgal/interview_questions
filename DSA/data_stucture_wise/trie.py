import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        temp = self.root
        for char in word:
            temp = temp.children[char]
        temp.isEnd = True
    
    def isWord(self, word):
        temp = self.root
        for char in word:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return temp.isEnd

trie : Trie = Trie()
trie.addWord("ABC")
trie.addWord("ABDC")
print(trie.isWord("ABC"))
print(trie.isWord("ABCD"))
print(trie.isWord("ABDC"))
print(trie.isWord("ABD"))