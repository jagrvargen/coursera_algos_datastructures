# Uses python3
import time

def pairwisemega(a):
    max = 0
    submax = 1
    start = time.time()
    if a[max] < a[submax]:
        max = 1
        submax = 0

    for i in range(len(a)):
        if a[i] > a[max]:
            max = i
        if a[i] < a[max] and a[i] > a[submax]:
            submax = i
    end = time.time()
    print("Pairwisemega got {} in {} secs".format(a[max] * a[submax], end - start))
    return (a[max] * a[submax])
