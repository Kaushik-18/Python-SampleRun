
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


def arrays_intersection(arr1 ,arr2):
    unique = set()
    index1,index2 = 0,0
    arr1.sort()
    arr2.sort()
    while index1 < len(arr1)  and index2 < len(arr2) :
        if arr1[index1] < arr2[index2] :
            index1 += 1
        elif arr2[index2] < arr1[index1] :
            index2 += 1
        else :
            unique.add(arr1[index1])
            index1 += 1
            index2 += 1
    return unique

def reverseVowels(value):
    vowel_map = ['a', 'e', 'i', 'o', 'u']
    letters = list(value)
    i, j = 0, len(value)-1
    while(i<j):
        while value[i] not in vowel_map and i <j:
            i += 1
        while value[j] not in vowel_map and i< j:
            j -= 1
        temp = letters[i]
        letters[i] = letters[j]
        letters[j] = temp 
        i+=1
        j-=1
    return ''.join(letters)

print(reverseVowels('hello'))


def delete_earn(elements):
    max_value = 0 
    elements.sort()
    if len(elements) == 1 :
        max_value = max_value + elements[0]

    deleted_vals = []

    for i in elements :
                
        pass

    def search_number_backs(value) :
        mid =  (len(elements) -1) //2
        left ,right = 0  ,len(elements) -1 
        while(left < right) :
            if  value < elements[mid] :
                right = mid
            elif value > elements[mid] :
                left = mid 
            elif value == elements[mid]:
                return True
        return False    

        pass


    pass








        




