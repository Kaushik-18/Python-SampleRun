# min repeats of A so that B is a substring , else return -1
def find_min_repeats(A,B) :
    times = -(- len(B) -1 // len(A) + 1)
    for i in range(2):
        if B in A * (times + i):
            return times + i
    return -1        

# max path length in bianry tree such that all values in path are equal

class Node :
    def __init__(self ,value):
        self.left = None
        self.right = None
        self.value = value

def findUniPath(root) :
    max_path = 0 
    
    def traverse(max_path , root) :
        if root is None :
            return max_path
        left_path = traverse(max_path , root.left) 
        right_path = traverse(max_path ,root.right)
        left_path = left_path + 1 if root.left and root.left.value == root.value else  0
        right_path = right_path + 1 if root.right and root.right.value == root.value else  0
        max_path = max(max_path , left_path + right_path)
        return max_path

    traverse(max_path , root)
    return max_path







    