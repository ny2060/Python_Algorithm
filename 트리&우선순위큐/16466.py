import sys

n= int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))


a.sort()

x = 1
for i in a:
    if i == x: 
        x += 1 
    else:
        print(x)
        sys.exit(0)


           
   
     


