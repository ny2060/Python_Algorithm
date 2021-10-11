import sys

n = int(input())

dp=[0]*(n+1)

t=[0]*n
p=[0]*n
for i in range(n):
    t[i],p[i]=map(int,input().split())

# 오늘 하는 것 : dp[day+t[day]]+p[day]
# 안하는 것 : dp[day+1]
# dp 에는 제일 고가의 수익을 저장
answer=0
for i in range(n):
    answer = max(answer,dp[i])

    if i+t[i]>n:
        continue
    
    dp[i+t[i]]=max(dp[i+1],answer+p[i])

print(max(dp))

# 오늘 날에는 dp[day]=max(dp[day+1],dp[day+T[day]]+p[day])
# day 에서 시작해서 퇴사일까지의 수익읠 최댓값을 dp에 저장



