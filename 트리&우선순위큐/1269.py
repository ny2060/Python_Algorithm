import sys

n,m=map(int,sys.stdin.readline().split()) #집합 두개의 각 원소 개수

a= set(map(int,sys.stdin.readline().split())) #a의 원소
b= set(map(int,sys.stdin.readline().split())) #b의 원소

# set 집합 자료형 순서가 없고 중복적인 요소 허용x

print(len(a-b)+len(b-a))
       
