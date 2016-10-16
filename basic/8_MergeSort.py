def mergesort(array):
    if len(array) < 2:
        return array
    result = []          # moved!
    mid = int(len(array)/2)
    y = mergesort(array[:mid])
    z = mergesort(array[mid:])
    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    return result

print (mergesort([3,7,2,7,1]))
