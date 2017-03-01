from collections import Counter


def find_longest(inputs, word_dict):
    input_count = Counter(inputs)
    largest_word = []
    for word in word_dict:
        word_count = Counter(word)
        is_append = True
        for w in word_count.keys():
            if not input_count.get(w):
                is_append = False
                break
            elif input_count[w] < word_count[w]:
                is_append = False
                break
        if is_append:
            largest_word.append(word)

    print(sorted(largest_word, key=len, reverse=True)[0])


find_longest('abpcplea', ["ale", "apple", "monkey", "plea"])
