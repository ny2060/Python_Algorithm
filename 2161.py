from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline())

for i in range(n):
  queue.append(i+1)

# 카드가 한장 남을 때까지 반복.
while(len(queue)>1):
  print(queue.popleft())
  queue.append(queue.popleft())

print(queue[0])