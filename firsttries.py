import itertools




# problem 2
# N = int(input())
#
# values = input()
#
# inputValList = values.split()
#
# selections = int(input())
#
# indexes = set()
# for i,x  in enumerate(inputValList):
#     if x == 'a':
#         indexes.add(i+1)
#
# combinations = itertools.combinations(range(1,N+1 ),selections)
#
# combinations = list(combinations)
#
# reqValues = 0
#
# for x in combinations :
#     if len(set.intersection(indexes,set(x))) > 0:
#         reqValues +=1
#
# print(reqValues)
#
# probability = reqValues/len(combinations)
#
# print(probability)

#problem 1
# map and lambda expressions
# list(map(lambda x: print(x,end=''),range(1,N+1)))

#problem 2
from collections import Counter
n  = int(input())
wordarray  = [input() for i in range(n) ]

print(*enumerate(wordarray))

# counts = dict()
# for i in items:
#     counts[i] = counts.get(i, 0) + 1


