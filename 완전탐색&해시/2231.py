import sys

#분해합 구하는 함수
def deSum(n):
    num=str(n)
    s=n
    for i in range(len(num)):
        s=s+int(num[i])
    return s

# 생성자 구하는 함수
def deCon(m):
    for i in range(m):
        if m ==deSum(i):
            return i


N=int(sys.stdin.readline())
print(deCon(N))