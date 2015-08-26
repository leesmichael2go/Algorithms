#https://www.hackerrank.com/challenges/extra-long-factorials
N = int(input())
product = 1
for num in range(1,N+1):
    product *= num
print(product)
