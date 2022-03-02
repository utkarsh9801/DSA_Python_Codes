def RecursivePower(n, power = 1):
    if power == 1:
        return n
    else:
        return n * RecursivePower(n, power - 1)

def IterativePower(n, power = 1):
    tot = 1
    for i in range(power):
        tot*=n
    return tot

#Calcuate the memory and time usage of the recursive and iterative power function
import time
import sys
sys.setrecursionlimit(1000000)

#Recursive Power
start = time.time()
(RecursivePower(2, 3000))
end = time.time()
print("Recursive Power: " + str(end - start))

#Iterative Power
start = time.time()
(IterativePower(2, 3000))
end = time.time()
print("Iterative Power: " + str(end - start))



