#https://www.hackerrank.com/challenges/simple-array-sum
N = int(input())
A = [int(x) for x in input().split()]
sum = 0
for n in A:
    sum += n
print(sum)