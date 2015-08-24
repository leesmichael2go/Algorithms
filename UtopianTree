#https://www.hackerrank.com/challenges/utopian-tree
T = int(input()) #number of test cases
heights = []

for i in range(0,T):
    cycles = int(input())
    height = 1
    if cycles == 0:
        heights.append(1)
    else:
        while cycles > 1:
            height *= 2
            height += 1
            cycles -= 2
        if cycles == 1:
            height *= 2
            cycles -= 1
        heights.append(height)
for h in heights:
    print(str(h))