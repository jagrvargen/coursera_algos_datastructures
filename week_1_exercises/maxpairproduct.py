# Uses python3
'''
n = list(input())
a = [int(x) for x in input().split()]
'''
import time

def maxpairfast(a):
    index_1 = 0
    start = time.time()
    for i in range(1, len(a)):
        if a[i] > a[index_1]:
            index_1 = i

    if index_1 == 0:
        index_2 = 1
    else:
        index_2 = 0

    for i in range(1, len(a)):
        if i != index_1 and a[i] > a[index_2]:
            index_2 = i
    end = time.time()
    print("maxpairfast got {} in {} secs".format(a[index_1] * a[index_2], end - start))

    return (a[index_1] * a[index_2])
