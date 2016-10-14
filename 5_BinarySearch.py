def binary_search(input_array, value):
    mid = int((len(input_array)/2))
    Found = False
    if input_array[mid]>value:
        mid = 0
        while input_array[mid]<value:
            mid +=1
            if input_array[mid] == value:
                Found = True
    else:
        while input_array[mid]<value:
            mid +=1
            if input_array[mid] == value:
                Found = True
    if Found:
        return mid
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
