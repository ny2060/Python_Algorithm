import sys

t = int(input()) # test case
graph = []
count =0

for _ in range(t):
    n ,m , k =map(int,input().split()) # 가로 , 세로

    for _ in range(m):
         graph.append([0]*n)

    for i in range(k):
        x,y=map(int,input().split())
        graph[y,x]=1

    for i in range(m):
        for j in range(n):
            if graph[i][j]==1:
                search(i,j)
                count+=1

    print(count)

        


def search(x,y):
    if (x<0 or x>=m or y<0 or y>=n):
       return

    if graph[x][y]==1:
        graph[x][y]=0

    search(x+1,y)
    search(x,y+1)
    search(x-1,y)
    search(x,y-1)
