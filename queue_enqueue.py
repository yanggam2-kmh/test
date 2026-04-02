SIZE = 5
queue = [None for i in range(SIZE)]
front = rear = -1

def is_full():
    if(rear == SIZE -1):
        return 1
    else:
        return 0

def enqueue(data):
    global rear
    if(is_full()):
        print("큐가 포화상태입니다")
        return
    rear += 1
    queue[rear] = data

def print_queue():
    print("--현재 큐의 상태 출력--")
    print("[",end = " ")
    for i in range(SIZE):
        print(queue[i], end = " ")
    print("]")
    print("front:", front, ",rear:", rear)

enqueue('A'); print_queue(); enqueue('B'); print_queue(); enqueue('C'); print_queue();
enqueue('D'); print_queue(); enqueue('E'); print_queue(); enqueue('F'); print_queue();
