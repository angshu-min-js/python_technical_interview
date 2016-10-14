def mergesort(x):
    if len(x) < 2:
        return x
    result = []          # moved!
    mid = int(len(x)/2)
    y = mergesort(x[:mid])
    z = mergesort(x[mid:])
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
