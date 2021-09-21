from sys import stdin
from itertools import combinations
# 카드 개수와 기준 점
n,m = map(int,input().split())

list=list(map(int,stdin.readline().split()))

big=0

for i in combinations(list,3):
  target=sum(i)
  if target>big and target<=m:
    big=target

print(big)
