import itertools

length = int(input())
numberlist = []

for i in range(length):
    numberlist.insert(i, int(input()))

print(*itertools.combinations(numberlist, 3))

print(numberlist)


def permutate(wordsarray, length):
    if length == 1:
        print(wordsarray)
    else:
        for i in range(length):
            wordsarray[i], wordsarray[length - 1] = wordsarray[length - 1], wordsarray[i]
            permutate(wordsarray, length - 1)
            wordsarray[i], wordsarray[length - 1] = wordsarray[length - 1], wordsarray[i]
