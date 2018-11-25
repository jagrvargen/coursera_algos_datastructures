# Uses python3

def lcm_brute(a, b):
    '''
       Finds the least common multiple of two non-negative integers using
       a brute force algorithm.
       Constraints: 1 <= a, b <= 2 * 10**9
    '''
    if a < b:
        a, b = b, a

    for i in range(a, (a * b + 1)):
        if i % a == 0 and i % b == 0:
            return i

#print(lcm_brute(int(input()), int(input())))
