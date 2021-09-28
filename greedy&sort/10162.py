import sys


food=int(sys.stdin.readline())

time=[300,60,10]

time=sorted(time,reverse=True)#내림차순으로 정렬
if food%time[-1] !=0:
    print(-1)
    
else:
    for i in time:
        print('%d' %(food//i)
        if food >=i:
            food -= i        
