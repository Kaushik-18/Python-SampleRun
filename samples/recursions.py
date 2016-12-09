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


def calculate_step_ways(num_of_steps):
    if num_of_steps == 0:
        return 1
    if num_of_steps < 0:
        return 0

    return calculate_step_ways(num_of_steps - 1) + calculate_step_ways(num_of_steps - 2) + calculate_step_ways(
        num_of_steps - 3)
