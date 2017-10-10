def longest_subsequence_cont_length(nums) :
    #[1,3,5,4,7]  longest is [1,3,5] not [1,3,5,7]  since 4,7 not continous
    max_len , i = 0,0
    while i < len(nums) :
        curr = 1
        while i+1 < len(nums) and nums[i] < nums[i+1] :
            curr,i =  curr +1 , i+1
        max_len =  max(max_len , curr)    
        i =  i+1
    return max_len    

def find_number_longest_increasing_sequences(nums):
    # [1,3,5,4,7] longest are [1,3,5,7] and [1,3,4,7] so answer is 2
    pass    


'''You are asked to cut off trees in a forest for a golf event. The forest is represented 
as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through,
 and this positive number represents the tree's height.
You are asked to cut off all the trees in this forest in the order of tree's height 
- always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).
You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.
You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:
Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6'''
def cutOffTrees(forest) :
    pass

'''Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to 
build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify 
exactly one character into another character 
in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:You may assume that all the inputs are consist of lowercase letters a-z.'''

class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
