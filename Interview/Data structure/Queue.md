# 자료구조 큐 
## 개념
- 선입선출 (FIFO)의 자료구조. 대기열이라고도 한다.    
- 데이터가 들어오는 위치는 가장 뒤(Rear or Back)에 있고, 데이터가 나가는 위치는 앞(Front)에 있어서 먼저 들어오는 데이터가 먼저 나가는 형태이다.    
- 데이터가 입력된 시간 순서대로 처리해야 할 필요가 있는 상황에 이용한다.

## 구현
### 파이썬 리스트 사용

```
class Queue(list):
    # enqueue => insert
    # dequeue => delete

    def __init__(self):
        self.queue = []
    
    def enqueue(self, n):
        self.queue.append(n)

    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    listQueue = Queue()
    listQueue.enqueue(1)
    listQueue.enqueue(2)
    listQueue.enqueue(3)
    listQueue.printQueue()
    listQueue.dequeue()
    listQueue.printQueue()

```

### collections.deque 사용
앞과 뒤, 양방향에서 데이터를 처리할 수 있음
```
from collections import deque

dq = deque([])

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
dq.append(5)
print(dq)

print(dq.popleft()) #왼쪽에서 pop
print(dq.pop())     #오른쪽에서 pop
print(dq)
```


