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


# find_longest('abpcplea', ["ale", "apple", "monkey", "plea"])


# longest substring
def lengthOfLongestSubstring(s):
    start = 0
    last = 0
    x = {}
    for i in range(len(s)):
        if s[i] in x and start <= x[s[i]]:
            start = x[s[i]] + 1
        else:
            last = max(last, i - start + 1)
        x[s[i]] = i
    return last


print(lengthOfLongestSubstring("abcabcbb"))

value = input()

# Output YES if string  can be converted to a "valid" string by removing less than
# or equal to one character.
# Else, output NO.
# Sample Input
# aabbcd
# Sample Output
# NO
from collections import Counter


def calculate(vals):
    counts = Counter(vals)
    # print(counts)
    val_set = counts.values()
    val_counts = Counter(val_set)
    # print(val_counts)
    if len(val_counts) == 1:
        print('YES')
    elif len(val_counts) == 2 and 1 in val_counts and val_counts[1] == 1:
        print('YES')
    elif len(val_counts) == 2 and val_counts[max(val_counts.keys())] == 1:
        print('YES')
    else:
        print('NO')


def convert_string_to_number(inputs):
    number_map = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    final_number = 0
    for x in inputs:
        if x == '-' or x == '+':
            continue
        elif x in number_map.keys():
            final_number = final_number * 10 + number_map[x]
        else:
            raise ValueError("Invalid Inputs")


class BinaryMiddleTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.middle = None

    def insert(self, value, root):
        if root is None:
            return BinaryMiddleTree(value)

        if root.root > value:
         root.left = self.insert(value, root.left)

        else:
         root.right = self.insert(value, root.right_node)

         return node
