'''n = int(input())
a = [int(i) for i in input.split()]
'''

def maxpairnaive(a):
    product = 0

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            product = max(product, a[i] * a[j])
    print(product)
    return product
