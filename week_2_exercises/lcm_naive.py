def lcm_naive(a, b):
    if a < b:
        a, b = b, a

    min = a * b
    for i in range(min, a, -1):
        if i % a == 0 and i % b == 0:
            min = i

    return min

print(lcm_naive(int(input()), int(input())))
