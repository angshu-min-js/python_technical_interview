def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[len(array)-1]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)  # + operator to join lists
    else:  # if just return the array.
        return array

print (quicksort([3,7,2,7,1]))
