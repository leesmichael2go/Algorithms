#https://www.hackerrank.com/challenges/chocolate-feast
T = int(input())
for i in range(T):

    N,C,M = map(int,input().split())
    answer = 0
    # Compute Answer
    wrappers = 0
    bought = int(N/C)
    answer += bought
    wrappers += bought
    while wrappers >= M:
        free = int(wrappers/M)
        answer += free
        wrappers = wrappers%M
        wrappers += free
    print(answer)
