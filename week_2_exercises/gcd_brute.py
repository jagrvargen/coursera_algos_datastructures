def gcd_brute(a, b):
    ''' Brute force greatest common divisor. '''
    max_d = 1

    if a < b:
        a, b = b, a

    for i in range(2, a):
        if a % i == 0 and b % i == 0:
            max_d = i

    return max_d

# print(gcd_brute(int(input()), int(input())))
