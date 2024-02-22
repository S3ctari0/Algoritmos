# Ordenamiento Burbuja

def burbuja_orden(array):
    for i in range(len(array)-1):
        for j in range(len(array)):
            while array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                burbuja_orden(array)
    return array

print(burbuja_orden([2, 4, 5, 1, 8, 3]))


#Selection Sort

def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array

print(selection_sort([2, 4, 5, 1, 8, 3]))

