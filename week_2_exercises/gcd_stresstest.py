#!/usr/bin/env python3
import random
import time

from gcd_brute import gcd_brute
from euclid_gcd import euclid_gcd

def gcd_stresstest():
    ''' Stress test for gcd '''
    
    for i in range(20):
        a = random.randint(1, 999999999)
        b = random.randint(1, 999999999)

        start_time_1 = time.time()
        print("gcd bruteforce input: {} {} -- output: {}".format(a, b, gcd_brute(a,b)))
        end_time_1 = time.time()
        print("bruteforce time: {}\n".format(end_time_1 - start_time_1))

        start_time_2 = time.time()
        print("euclidean gcd input: {} {} -- output: {}".format(a, b, euclid_gcd(a,b)))
        end_time_2 = time.time()
        print("euclidean time: {}\n".format(end_time_2 - start_time_2))

gcd_stresstest()
