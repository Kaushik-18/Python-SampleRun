converts_list = '0123456789ABCDEF'


def convert_numbers(mode, number):
    if number < mode:
        return converts_list[number]
    else:
        return convert_numbers(mode, number // mode) + converts_list[number % mode]


def reverse_string(inputs):
    if len(inputs) == 1:
        return inputs
    else:
        return inputs[len(inputs) - 1] + reverse_string(inputs[:len(inputs) - 1])


def permutate(wordsarray, length):
    if length == 1:
        print(wordsarray)
    else:
        for i in range(length):
            wordsarray[i], wordsarray[length - 1] = wordsarray[length - 1], wordsarray[i]
            permutate(wordsarray, length - 1)
            wordsarray[i], wordsarray[length - 1] = wordsarray[length - 1], wordsarray[i]







