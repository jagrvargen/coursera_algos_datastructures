# Uses python3

def euclid_gcd(a, b):
    '''
       Computes the greatest common divisor of two non-negative integers.
    '''
    if a < b:
        a, b = b, a
    if b == 0:
        return a

    a_prime = a % b

    return euclid_gcd(b, a_prime)

# print(euclid_gcd(int(input()), int(input())))
