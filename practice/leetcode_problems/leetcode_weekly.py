
import math

#given sequence from 1 to n ,and non-requred value k
# find max sum possible which is not equal to k visiting sequentially
def find_max_collection2(n , k) :
    sum = n * (n+1)//2
    index  = (math.sqrt(1+8*k) -1 )/2
    if  index == math.floor(index) and index <= n :
        sum-=1     
    return sum    


# check if ipv4 or ipv6
# TODO break up into smaller check functions
# TODO for ipv6 token check ,check if alphabet values are valid
def check_ip(ipval) :
    codes =  ipval.split('.')
    if len(codes) != 4 and len(codes)!= 8:
        return "Neither"
    elif len(codes) == 4 :
        for code in codes :
            if code[0] == '0':
                return 'Neither'
            elif len(code) != 4 :
                return "Neither"
            elif code.isdigit() == False :
                return "Neither"
            else :
                return "IPV4" 
    else :
        for code in codes :
            if len(code) !=4 :
                if code[0] != 0 :
                    return "Neither"
        return "IPV6"        

# remove target value from  arrray ..without sorting in O(n)
def remove_target_elements(values ,target):
    start,end  =  0 , len(values) -1
    while start < end :
        if values[start] == target :
            values[start] ,values[end] ,end = values[end] ,values[start] , end -1
        else :
            start += 1

    return end + 1

#majority element appearing more than n//2 times O(n)
def find_majority_element(values) :
    current =  values[0]
    counter = 0
    for val in values :
        if current == val :
            counter += 1
        else :
            if counter == 0 :
                current = val
                counter += 1
            else :
                counter -= 1
    return current            

# find indices of numbers in array which add up to given target
def findTwoSum(target ,values):
    holder={}
    answer=[]
    for index in range(values) :
        check_value=target-values[index]
        if check_value in holder.keys() :
            return (holder[check_value],index)
        else :
            holder[check_value] = index

# as above,but find indices if input is sorted 
# with 2 pointer 
def findTwoSumSorted(target , values) :
    left,right=0,len(values)-1
    while left < right :
        check=values[left]+values[right]
        if check==target:
            return (left,right)
        elif check<target:
            left+=1
        else:
            right-=1
    return (0,0)

#input is BST, check if 2 values exsit such that sum is target
#If not a BST, we could just a BFS with hash map,set
# use the inorder traversal gives sorted list property of BST. 
class TreeNode :
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def checkTwoSumBinaryTree(target,root):
    if root is None :
        return False
    pass







        
            












                








