#!/usr/bin/env python3
import random
import time

from lcm_brute import lcm_brute
from lcm import lcm

def lcm_stresstest():
    '''
       Stress test for lowest common multiplier functions.
    '''
    x = True
    while x:
        a = random.randint(1, (2 * 10**9 + 1))
        b = random.randint(1, (2 * 10**9 + 1))
        print('check\n')
        start_1 = time.time()
        brute = lcm_brute(a, b)
        end_1 = time.time()
        print("lcm bruteforce input: {} {} -- output: {}".format(a, b, brute))
        print("bruteforce took {} secs\n".format(end_1 - start_1))

        start_2 = time.time()
        optimized = lcm(a, b)
        end_2 = time.time()
        print("lcm optimized input: {} {} -- output: {}".format(a, b, optimized))
        print("optimized took {} secs".format(end_2 - start_2))

        if brute != optimized:
            print("MISMATCH\n")
            x = False

lcm_stresstest()
