#locating value within array
#input is a value and an array, output is the index of the array at which the value appears
#output limited to first appearance of the value sought
V = input()
leng = int(input())
array = input().split()
i = 0
while i < leng:
    if V == array[i]:
        print(i)
        break
    else:
        i += 1
    
