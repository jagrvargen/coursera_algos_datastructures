#!/usr/bin/env python3
import random
import time
from fibonaccinaive import fibonacci_naive
from fibonacci_dynamic import fibonacci
from fibonacci_last_digit_simple import fib_last_dig_simple

def stress_test():
    '''
       Tests the fibonacci sequence generators with randomly generated
       lengths.
    '''
    n = random.randint(0,40)
    for i in range(n):
        start_1 = time.time()
        print("naive input: {} -- output: {}".format(i, fibonacci_naive(i)))
        end_1 = time.time()
        print('naive time: {}\n'.format(end_1 - start_1))

        start_2 = time.time()
        print("memoized input: {} -- output: {}".format(i, fibonacci(i)))
        end_2 = time.time()
        print('memoized time: {}\n'.format(end_2 - start_2))

        start_3 = time.time()
        print("last digit input: {} -- output {}".format(i, fib_last_dig_simple(i)))
        end_3 = time.time()
        print('last digit runtime: {}\n'.format(end_3 - start_3))

stress_test()
