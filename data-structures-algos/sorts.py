# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
def insertionSort(array):
    for i in range(1, len(array)):
        currentPosition = i
        currentValue = array[i]

        while currentPosition >= 1 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition - 1]
            currentPosition -= 1

        array[currentPosition] = currentValue

    return


# insertion sort is simple shell sort with index 1.
def shellSort(array):
    shellIndex = len(array) // 2

    while (shellIndex > 0):
        print(shellIndex)
        for index in range(shellIndex):
            # skip by shell index ,
            for i in range(index + shellIndex, len(array), shellIndex):
                currentPosition = i
                currentValue = array[i]
                # if currentPosition is less than the gap ,comparison will not be possible as index will be negative
                while currentPosition >= shellIndex and array[currentPosition - shellIndex] > currentValue:
                    array[currentPosition] = array[currentPosition - shellIndex]
                    currentPosition = currentPosition - shellIndex

                array[currentPosition] = currentValue

        shellIndex = shellIndex // 2

    return


def mergesort(array):
    if len(array) > 1:
        midpoint = len(array) // 2
        array_left = array[:midpoint]
        array_right = array[midpoint:]

        mergesort(array_left)
        mergesort(array_right)

        i, j, k = 0, 0, 0
        while i < len(array_left) and j < len(array_right):
            if array_left[i] < array_right[j]:
                array[k] = array_left[i]
                k += 1
                i += 1
            elif array_left[i] > array_right[j]:
                array[k] = array_right[j]
                k += 1
                j += 1
        while j < len(array_right):
            array[k] = array_right[j]
            k += 1
            j += 1
        while i < len(array_left):
            array[k] = array_left[i]
            k += 1
            i += 1


def quicksort(array, firstindex, lastindex):
    if firstindex < lastindex:
        left_marker = firstindex
        right_marker = lastindex
        pivot = array[(lastindex + firstindex) // 2]
        while left_marker <= right_marker:
            while array[left_marker] < pivot:
                left_marker += 1
            while array[right_marker] > pivot:
                right_marker -= 1
            if left_marker <= right_marker:
                temp = array[left_marker]
                array[left_marker] = array[right_marker]
                array[right_marker] = temp
                left_marker += 1
                right_marker -= 1
                # if left_marker < lastindex:
            quicksort(array, left_marker, lastindex)
            # if firstindex < right_marker:
            quicksort(array, firstindex, right_marker)


testarray = [77, 2, 3, 43, 12, 5, 4, 8, 100, 50, 77, 99, 200, 98, 67]
quicksort(testarray, 0, len(testarray) - 1)
print(testarray)
