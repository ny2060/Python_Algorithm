import sys


k= int(input()) #입력 횟수를 받음

dp = [0]*(k+1) # 1부터 접근 편하게 하기 위해서


dp[1]=1 # 한번 눌렀을 경우 b

for i in range(2,k+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[k-1],dp[k])
