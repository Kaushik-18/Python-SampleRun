# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"] Leetcode 212

class Trie :
    def __init__(self):
        self.nodes  =  collections.defaultdict(Trie)
        self.isword = False

    def add(self , word):
        node = self
        for letter in word :
            node  = node.nodes[letter]
        self.isword = True

def search_board(word_list , board) :
    trie  =  Trie()
    for word in word_list :
        trie.insert(word)
    seen_vals = [[False]*len(board[0])  for i in range(len(board))]
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            scan_board(i,j,board,res,trie,'',seen_vals)


def scan_board(x, y , board , accumlator , node , result ,seen_vals) :
    if i < 0 or j < 0 or j >= len(board) or i >= len(board[0]) :
        return
    if node.isword :
        accumlator.append(result)

    if not seen_vals[x][y] and board[i][j] in node :
        result += board[x][y]
        seen_vals[x][y] = True
        scan_board(x+1 ,y ,board , accumlator , node[board[x][y]],result,seen_vals)
        scan_board(x-1 ,y ,board , accumlator , node[board[x][y]],result,seen_vals)
        scan_board(x ,y+1 ,board , accumlator , node[board[x][y]],result,seen_vals)
        scan_board(x ,y-1 ,board , accumlator , node[board[x][y]],result,seen_vals)
        seen_vals[x][y] = False
