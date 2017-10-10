# used in applications like ip tables,auto complete
# using defalutdict here so that a default value is returned
import collections
class TrieNode :
    def __init__(self):
        self.list  = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie :
    def __init__(self) :
        self.root = TrieNode()

    def addWord(self ,word) :
        node = self.root
        for curr in word :
            node  = node.list[curr]
        node.isWord = True

    def search(self , word) :
        node = self.root
        for letter in word :
            node  =  node.list[letter]
            if node is None :
                return False
        return node.isWord

    def starts_with(self,prefix) :
        node  =  self.root
        for letter in word :
            node =  node.list[letter]
            if node is None :
                return False
        return True
