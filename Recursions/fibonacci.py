"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
"""

def iterFibonacci(n):
    fib = [0, 1]
    first = 0
    assert 0 <= n == int(n), "Number should be positive integer"
    if n == 1:
        return first
    if n == 2:
        return fib
    for i in range(3,n+1):
        fib.append(fib[-1]+fib[-2])
    return fib


print(*iterFibonacci(10), sep=", ")