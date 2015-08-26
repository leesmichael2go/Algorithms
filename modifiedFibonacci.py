#https://www.hackerrank.com/challenges/fibonacci-modified
from collections import deque
triple = deque(maxlen = 3)
abc = [int(x) for x in input().split()]
ab = abc[:2]
a = ab[0]
b = ab[1]
c = a + b**2
triple.append(a)
triple.append(b)
triple.append(c)

n = abc[2]
i = 3
while i < n:
    triple.append(triple[1] + triple[2]**2)
    i += 1
print(triple[2])
