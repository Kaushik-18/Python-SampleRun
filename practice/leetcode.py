# spiral matrix

# matrix = [[1, 2, 4], [4, 5, 6], [7, 8, 9]]

def print_spiral(darray):
    row_index = 0
    column_index = 0
    results = ''

    no_of_rows = len(darray)
    no_of_columns = len(darray[0])

    while no_of_columns > 0 and no_of_rows > 0:

        if no_of_rows == 1:
            for i in range(no_of_columns):
                results += str(darray[row_index][column_index + i])
            break

        if no_of_columns == 1:
            for i in range(no_of_rows):
                results += str(darray[row_index + i][column_index])
            break

        for i in range(no_of_columns - 1):
            results += str(darray[row_index][column_index])
            column_index += 1

        for i in range(no_of_rows - 1):
            results += str(darray[row_index][column_index])
            row_index += 1

        for i in range(no_of_columns - 1):
            results += str(darray[row_index][column_index])
            column_index -= 1

        for i in range(no_of_rows - 1):
            results += str(darray[row_index][column_index])
            row_index -= 1

        no_of_rows -= 2
        no_of_columns -= 2
        row_index += 1
        column_index += 1

    return results


# print(print_spiral(matrix))


def merge_intervals(interval_list):
    interval_list = sorted(interval_list, key=lambda val: val[0])
    start = interval_list[0][0]
    end = interval_list[0][1]
    result = []
    for i in range(len(interval_list)):
        if interval_list[i][0] <= end:
            end = max(end, interval_list[i][1])
        else:
            result.append([start, end])
            start = interval_list[i][0]
            end = interval_list[i][1]

    result.append([start, end])
    return result


# print(merge_intervals([[8, 10], [1, 3], [2, 6], [15, 18]]))


# find length of longest subsequence , find number of deletions so that 2 strings are the same

def find_longest_sequence(A, B):
    m, n = len(A), len(B)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    res = m - dp[m][n] + n - dp[m][n]
    return dp[m][n]


# print(find_longest_sequence('set', 'eats'))

def find_unique_in_list(list1, list2):
    num_map = {}
    for i in list1:
        if i in num_map:
            num_map[i] += 1
        else:
            num_map[i] = 1

    for i in list2:
        if i in num_map:
            num_map[i] += 1
        else:
            num_map[i] = 1

    for k, val in num_map.items():
        if val == 1:
            return k




