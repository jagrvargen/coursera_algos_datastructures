# Uses python3

def fibonacci(n, memo={0: 0, 1: 1}):
    '''
       Outputs nth number in Fibonacci sequence using memoization.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]

#print(fibonacci(int(input())))
