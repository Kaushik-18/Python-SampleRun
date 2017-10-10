#given a string 's' , delete at most one charecter,determine if it can 
#be made into palindrome

def check_palindrome(s):
    '''checking if string with given start and end is a palindrome'''
    def is_valid_palindrome(check_string,start,end):
        while(start < end) :
            if check_string[start] == s[end] :
                start += 1
                end -= 1
            else :
                return False  
        return True

    start ,end =  0 , len(s) - 1
    while start < end and s[start] == s[end]:
        start += 1
        end -= 1
    if start >= end :
        return True

    if is_valid_palindrome(s,start+1,end) or is_valid_palindrome(s,start,end-1):
        return True
    return False

#Map sum pairs. For a given string value pair 
#For the method insert, you'll be given a pair of (string, integer). 
# The string represents the key and the integer represents the value. 
# If the key already existed, 
# then the original key-value pair will be overridden to the new one.
#For the method sum, you'll be given a string representing the prefix, 
# and you need to return the sum of all the pairs' value 
# whose key starts with the prefix.

class TreeNode :
    def __init__(self,val,count=0) :
        self.children = {}
        self.val = val
        self.count = count

def search_prefix(node) :
        sum_fin = 0
        for c in node.children.keys() :
            sum_fin += search_prefix(node.children[c])
        return sum_fin + node.count 

class MapSum :
    def __init__(self) :
        self.root =  TreeNode('')

    def insert(self,key ,val) :
        current =  self.root
        for c in key :
            if c not in current.children :
                current.children[c] = TreeNode(c)
            current = current.children[c]
        current.count = val


    def sum(self,prefix):
        current = self.root
        for c in prefix :
            next_curr = current.children.get(c)
            if not next_curr :
                return 0
            current = next_curr
        return search_prefix(current)
   

''' sumer = MapSum()
sumer.insert("apple",3)
sumer.insert("app",2)
print(sumer.sum("ap")) '''

''' 
Given a string containing only three types of characters: '(', ')' and '*', 
write a function to check whether this string is valid. 
We define the validity of a string by these rules:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left 
parenthesis '(' or an empty string.
An empty string is also valid. '''

def checkValidParenth(evals):
    max ,min = 0,0 
    for c in evals :
        max  =  max - 1 if c == ")" else max + 1
        min =  min + 1 if c  == "(" else max(min - 1 ,0)
        if max < 0 :
            break 
    return min == 0    


print(checkValidParenth('(()'))

    
           



















