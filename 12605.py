import sys

n=int(sys.stdin.readline())

for i in range(n):
  word=sys.stdin.readline().split()
  print("Case #"+str(i+1)+":",end=" ")
  word.reverse()
  for j in range(len(word)):
    print(word[j],end=" ")
