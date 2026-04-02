SIZE = 5
Queue = ['A','B','C',None, None]
front = -1
rear = 2

def isEmpty():
    if(rear == front):
        return 1
    else:
        return 0

def deQueue():
    global front
    if(isEmpty()):
        print("큐가 공백 상태입니다")
        return
    front += 1
    delete_data = Queue[front]
    Queue[front] = None
    print("삭제할 데이터: ", delete_data)

def printQueue():
    print("--현재 큐의 상태--")
    print("[", end= " ")
    for i in range(SIZE):
        print(Queue[i], end = " ")
    print("]")
    print("front: ", front, "rear: ", rear)

print(Queue); deQueue(); print(Queue); deQueue(); print(Queue); deQueue(); print(Queue); deQueue();
