# Question : Dont get volunteered !
# knights_problem.py

# To check substitution cipher period (repetiton sequence length) comprising of
# Question : Hey I already did that.

def convert_numbers(mode, number):
    final_number = ''
    while number > 0:
        rem = number % mode
        number = number // mode
        rem_string = str(rem)
        final_number = rem_string + final_number
    return final_number


def find_random_end(n, b):
    num_len = len(n)
    num_list = []
    counter = 0
    while int(n) > 0:
        num_str_asc = ''.join(sorted(n))
        num_str_desc = ''.join(sorted(n, reverse=True))
        number_val = int(num_str_desc, base=b) - int(num_str_asc, base=b)
        number_val = convert_numbers(b, number_val)
        n = str(number_val)
        n = n.zfill(num_len)
        if n in num_list:
            counter += 1
        num_list.append(n)

        if counter == 3:
            index = num_list.index(n)
            flist = num_list[index:]
            return len(set(flist))

    if int(n) == 0:
        return 1


# find largest number divisible by 3 eg : [3,1,4,1] ans :- 4311 ,  l = [3, 1, 4, 1, 5, 9]  ans :- 94311
# Question : Please Pass the Coded Messages

def find_largest_by_three(nums_array):
    final_array = sorted(nums_array)
    queue_0 = [i for i in final_array if i % 3 == 0]
    queue_1 = [i for i in final_array if i % 3 == 1]
    queue_2 = [i for i in final_array if i % 3 == 2]
    final_array = []
    total_sum = sum(nums_array)
    if total_sum % 3 != 0:
        if total_sum % 3 == 1:
            if len(queue_1) > 0:
                queue_1.pop(0)
            elif len(queue_2) > 1:
                queue_2.pop(0)
                queue_2.pop(0)
            else:
                return 0

        elif total_sum % 3 == 2:
            if len(queue_2) > 0:
                queue_2.pop(0)
            elif len(queue_1) > 1:
                queue_1.pop(0)
                queue_1.pop(0)
            else:
                return 0

    if len(queue_0) > 0:
        final_array.extend(queue_0)
    if len(queue_1) > 0:
        final_array.extend(queue_1)
    if len(queue_2) > 0:
        final_array.extend(queue_2)

    final_array = sorted(final_array, reverse=True)
    final_number = ''
    for i in final_array:
        final_number += str(i)
    return int(final_number)


print find_largest_by_three([3, 1, 4, 1])
