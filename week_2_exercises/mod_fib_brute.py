# Uses python3

def mod_fib_brute(n, m):
    '''
       Computes the nth fibonacci number modulo m.
       Constraints: 0 <= n <= 10**18 and 2 <= m <= 10**5
    '''
    seq_len, fib_seq = series(m)
    assert (seq_len is not None)
    
    Fib_i = n % seq_len
    return fib_seq[Fib_i] % m
    

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

def series(m):
    '''
       Determines the length of the periodic sequence of F_i mod m
    '''
    series = []
    fib_seq = {}

    for i in range((m**2+1)):
        F_i = fibonacci(i)
        fib_seq[i] = F_i
        series.append(F_i % m)

    for i in range(2, len(series) // 2):
        if series[0:i] == series[i:2*i]:
            return i, fib_seq

    return None, None

#print(mod_fib(int(input()), int(input())))
