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
    if len(array) > 1 :
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
    i = firstindex
    j = lastindex
    pivot = array[lastindex + firstindex // 2]
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1
            j -= 1
    print(i, j, firstindex, lastindex)
    if (i < lastindex):
        quicksort(array, i, lastindex)
    if (firstindex < j):
        quicksort(array, firstindex, j)


testarray = [1, 0, 5, 4, 8, 100, 50, 77, 99]
mergesort(testarray)
print(testarray)
