#!/usr/bin/env python3
import random
import time

from mod_fib import mod_fib
from mod_fib_brute import mod_fib_brute

def mod_fib_stresstest():
    '''
       Stress test for mod_fib functions which determine the modulo of large
       fibonacci numbers.
    '''
    x = True

    while x:
        n = random.randint(0, 10**10)
        m = random.randint(2, 10**3)

        start_1 = time.time()
        mod_brute = mod_fib_brute(n, m)
        end_1 = time.time()
        print("brute force mod inputs: n == {} m == {} -- output: {}".format(n, m, mod_brute))
        print("brute force time: {} secs\n".format(end_1 - start_1))

        start_2 = time.time()
        mod_op = mod_fib(n, m)
        end_2 = time.time()
        print("optimized mod inputs: n == {} m == {} -- output: {}".format(n, m, mod_op))
        print("optimized time: {} secs\n".format(end_2 - start_2))

        if mod_brute != mod_op:
            x = False

mod_fib_stresstest()

'''
        start_1 = time.time()
        mod_brute = mod_fib_brute(n, m)
        end_1 = time.time()
        print("brute force mod inputs: n == {} m == {} -- output: {}".format(n,\
 m, mod_brute))
        print("brute force time: {} secs\n".format(end_1 - start_1))
'''
