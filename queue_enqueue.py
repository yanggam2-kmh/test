SIZE = 5
Queue = [None for i in range(SIZE)]
front = rear = -1

def isFull():
    if(rear == SIZE -1):
        return 1
    else:
        return 0

def enqueue(data):
    global rear
    if(isFull()):
        print("큐가 포화상태입니다")
        return
    rear += 1
    Queue[rear] = data

def printQueue():
    print("--현재 큐의 상태 출력--")
    print("[",end = " ")
    for i in range(SIZE):
        print(Queue[i], end = " ")
    print("]")
    print("front:", front, ",rear:", rear)

enqueue('A'); printQueue(); enqueue('B'); printQueue(); enqueue('C'); printQueue();
enqueue('D'); printQueue(); enqueue('E'); printQueue(); enqueue('F'); printQueue();
