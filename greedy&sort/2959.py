import sys

a,b,c,d=map(int,sys.stdin.readline().split())

list=[a,b,c,d]

#list.sort(reverse=True)

list=sorted(list,reverse=True)
print(list[1]*list[-1])
