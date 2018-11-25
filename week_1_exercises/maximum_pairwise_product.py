# Uses python3

n = int(input())
a = [int(i) for i in input().split()]

a = sorted(a)
print(a[-1] * a[-2])
