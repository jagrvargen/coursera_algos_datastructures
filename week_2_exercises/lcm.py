# Uses python3

def lcm(a, b):
    '''
       Finds the lowest common multiple between two non-negative integers.
    '''
    if a < b:
        a, b = b, a

    div = gcd(a, b)
    return a // div * b

def gcd(a, b):
    '''
       Finds the greatest common divisor between two non-negative integers.
    '''
    if b == 0:
        return a

    a_prime = a % b
    return gcd(b, a_prime)

# print(lcm(int(input()), int(input())))
