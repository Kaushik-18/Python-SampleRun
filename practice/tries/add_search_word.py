#search(word) can search a literal word or a regular expression string
#containing only letters a-z or .. A . means it can represent any one letter.

class Trie :
    __init__(self):
        self.child  =  collections.defaultdict(Trie)
        self.isWord =  False

class WordDict() :
    __init__(self) :
        self.root =  Trie()

    addWord(self ,word):
        node =  self.root
        for w in word :
            node =  node.child[w]
        node.isWord = True

    search(self, word):
        return search_dfs(self.root,word)

    search_dfs(node,word):
        for i  in len(word) :
            c  = word[i]
            if c == '.' :
                #since it can be any word
                for k in node.child :
                    if(search_dfs(node.child[k] , word[i+1:])):
                        return True
            return False
            elif  c not in node.child:
                    return False
            node = node.child
            return node.isWord
