def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)


# Test cases
print (get_fib(9))
print (get_fib(11))
print (get_fib(0))
'''
In practice if we were to use recursion to solve this problem we should use a hash table
to store and fetch previously calculated results. This will increase the space needed
but will drastically improve the runtime efficiency.
'''
