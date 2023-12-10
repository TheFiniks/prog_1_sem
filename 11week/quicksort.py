from random import randint


def quicksort(array):
    l = len(array)
    if l < 2:
        return array
    else:
        index = randint(0, l - 1)
        pivot = array[index]
        array.pop(index)
        left = [i for i in array if i < pivot]
        right = [j for j in array if j >= pivot]
        return [*quicksort(left), pivot, *quicksort(right)]

