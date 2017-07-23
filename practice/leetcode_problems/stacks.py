# function exclusive time
def exclusive_time(n , logs):
        ans = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)
            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return ans

#binary tree mirror image
class TreeNode():
    def __init__(self,value):
        self.left =  None
        self.right =  None
        self.value  =  value

def check_mirror_image(root):
    stack = []
    if root is None :
        return True
    stack = [root.left,root.right]
    while len(stack) > 0 :
         left  =  stack.pop()
         right = stack.pop()
         if left is None and right is None :
             continue
        elif left is None or right  is None :
            return False
        if left.val == right.val :
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        else :
            return False
    return True

#reverse polish notation
def reverse_polish(tokens):
    stack = []
    for t in tokens :
        if t not in ["+","-","*","/"] :
            stack.append(t)
        else :
            val1,val2 =  stack.pop() ,stack.pop()
            v3 = 0
            if t == '-':
                v3 =  val2 - val1
            elif t == '+':
                v3  = val2 + val1
            elif val == '*':
                v3 = val2*val1
            else :
                v3 = val2/val1
            stack.append(v3)
    return stack.pop()

# path simplification
def simplify_path(path) :
    vals = path.split()
    stack = []
    for v in vals :
        if v == '..' :
            if len(stack) > 0 :
                stack.pop()
        else :
            stack.append(v)
    return "/" + "/".join(stack)

    
