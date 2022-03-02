def recursiveFactorial(n):
    assert n >= 0 and int(n) == n, "The number should be positive and greater than 0"
    if n == 1:
        return 1
    return n * recursiveFactorial(n - 1)


def iterFactorial(n):
    tot = 1
    for i in range(1, n+1):
        tot*=i
    return tot

print(recursiveFactorial(-10))
print(iterFactorial(-10))