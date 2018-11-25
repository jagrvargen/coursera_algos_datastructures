def fib_last_dig_simple(n):
    '''
       Returns the last digit of the given fibonacci number.
    '''
    fib = {}
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n+2):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 10

    return fib[n]

print(fib_last_dig_simple(int(input())))
