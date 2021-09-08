import sys

N = int(sys.stdin.readline())

bar = list()

for _ in range(N):
    data = int(sys.stdin.readline())
    bar.append(data)

count = 0
start = 0

for i in range(1, N + 1):
    target = bar[-i]
    if (target > start):
        count += 1
        start = target

print("갯수", count)
