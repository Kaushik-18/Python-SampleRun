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


# Q 3 Bomb_Baby !

def validate(M, F):
    m = int(M)
    f = int(F)
    counter = 0
    while min(m, f) != 1:
        if m == f:
            return "impossible"
        if m > f:
            diff = m // f
            m %= f
            counter += diff
        else:
            diff = f // m
            f = f % m
            counter += diff

    counter = counter + f + m - 2
    return str(counter)


# print(validate("4", "7"))
#  Q 3B
# naive solution :- loop through and xor all previous ,problem will take a very long time o(n^2)
# we observe that if if we take xor over a range 0-a, there is a cycle corresponding to [a,0,a+1,1]
# so for xor over rage [a,b] , we use xor associative and commutative property
# eg:-   n  a^a+1^....^b   f(b)  = 1^2^3...^(a-1)+(a^ ... ^b)  which can be written as n = f(a-1) ^ f()b
def xor_for_ranges(x, y):
    def helper(x):
        check_cycle_array = [x, 1, x + 1, 0]
        cycle_pos = x % 4
        return check_cycle_array[cycle_pos]

    return helper(x - 1) ^ helper(y)


def check_sum(start, length):
    sub_length = length
    output = 0
    while sub_length > 0:
        output ^= xor_for_ranges(start, start + sub_length - 1)
        start = start + length
        sub_length -= 1
    return output


def test_xor(lengths):
    output = 0
    for i in range(lengths):
        output = output ^ i
        print(output)


# print(check_sum(0, 3))  # 032

# Q 3.3

def dp_answer(n, current_height, d):
    # at any step you have 2 options. The first option is to increase the height of the current step
    # you are on by adding one more brick, i.e., rec(left-1, curr+1) and the second option
    # is to create a new step whose height should be greater than curr ,i.e., rec(left-curr-1, curr+1)
    # ( you created a step of height curr+1 ). Now, left can never be negative ,
    #  thus if left<0 then return 0. And when left is 0 that means, we have created
    # a valid staircase,thus if left==0 then return 1.
    # This case: if dp[left][curr] !=-1 is just for memoization.
    # Now, rec( 212-1, 1 ) means a step of height 1 is created and it is the current step.
    # And for final answer 1 is subtracted because any valid staircase should contain at least 2 steps so,
    #  subtracting 1 for single step staircase.
    if n < 0:
        return 0
    if n == 0:
        return 1
    if d[n][current_height] != -1:
        return d[n][current_height]

    d[n][current_height] = dp_answer(n - (current_height + 1), current_height + 1, d) + \
                           dp_answer(n - 1, current_height + 1, d)

    return d[n][current_height]


def answer(n):
    ways = [[-1] * (n + 1) for i in range(n + 1)]
    return dp_answer(n - 1, 1, ways) - 1


# print(answer(200))
import itertools


def comboall(num_buns, num_required):
    r = []

    # Applying pegion rule
    f = list(itertools.combinations(range(num_buns), num_required))
    total = len(f) * num_required
    repeat_times = num_buns - num_required + 1
    f1 = list(itertools.combinations(range(num_buns), repeat_times))
    for i in range(num_buns):
        r.append([])

    for i in range(total // repeat_times):
        for j in f1[i]:
            r[j].append(i)

    return r

print(comboall(5,3))