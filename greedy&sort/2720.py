import sys

test_num=int(sys.stdin.readline())

test=[]


for _ in range(test_num):
    test.append(int(sys.stdin.readline()))
    



for i in test:
    result = i//25
    i -= 25*result

    result1 = (i%25)//10
    i -= 10*result1

    result2 = ((i%25)%10)//5
    i -= 5*result2

    result3 = (((i%25)%10)%5)//1
    i -= result3

    print(result,result1,result2,result3)
