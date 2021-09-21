import sys

L = int(sys.stdin.readline())

n = sys.stdin.readline().rstrip()

result=0
for i in range(L):
    result+=(ord(n[i])-96)*31**i

print(result %1234567891)