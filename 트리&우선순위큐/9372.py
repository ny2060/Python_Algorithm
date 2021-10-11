import sys
t = int(input())
for i in range(t):
    N, M = map(int, input().split()) #국가의 수와 비행기 종류
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())

    print(N-1)
