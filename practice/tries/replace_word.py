# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

class TriNode:
    def __init__(self) :
        self.children = collections.defaultdict(TriNode)
        self.isword = False

class WordReplace :
    def __init__(self) :
        self.root = TriNode()

    def add(self , word):
        node  =  self.root
        for letter in word :
            node  = self.children[letter]
        node.isWord = True

    def findWordRoot(self, word):
        pref = ''
        node  =  self.root
        for w in word :
            if w in node.children:
                node =  node.children[w]
                pref += w
                if node.isword == True :
                    return pref
            else :
                break
        return word

rev =  WordReplace()
root_dictionary = []
for word in root_dictionary :
    rev.add(word)

op_sentence = ''
for word in sentence.split() :
    root = rev.findWordRoot(word)
    op_sentence.append(' ').append(root)
