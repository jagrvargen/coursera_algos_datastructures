from maxpairproduct import maxpairfast
from maxpairwiseproductnaive import maxpairnaive
from maxpaironeandonehalf import pairwisemega
import random
x = True
while x:
    n = random.randint(2, 10)
    a = [random.randint(0,10000) for i in range(n)]

    print(a)

    result_1 = pairwisemega(a)
    result_2 = maxpairfast(a)
    if result_1 == result_2:
        print("OK")
    else:
        print("WRONG", result_1, result_2)
        x = False
