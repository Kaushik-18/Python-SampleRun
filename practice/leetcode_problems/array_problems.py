
#remove elements of given value given sorted list
def remove_all_given_vals(val_list,val):
    start ,end = 0 ,len(val_list)-1
    while start <= end:
        if val_list[start] == val :
            val_list[start] = val_list[end]
            val_list[end] = val
            end -= 1
        else:
            start += 1
    return end + 1

#find 3 numbers whose sum is closest to the given value and return the sum
def find_closest(v_list,value):
    v_list.sort()
    best_sum = v_list[0] + v_list[1] + v_list[2]
    for i in range(len(v_list)- 2):
        s = i + 1
        t = len(v_list) - 1
        while s < t:
            curr = v_list[i]+v_list[s]+v_list[t]
            if curr == value :
                return curr
            if curr < value :
                s+=1
            else:
                t-=1
            if abs(curr-value) < abs(best_sum-value):
                best_sum =curr
     return best_sum


# set of 4 numbers for target sum
def find_sum_four(nums,val):
    solution_set=[]
    nums.sort()
    for i in range(len(v_list)-3):
        pass

#
