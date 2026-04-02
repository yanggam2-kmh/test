SIZE = 5
queue = ['A','B','C',None, None]
front = -1
rear = 2

def is_empty():
    if(rear == front):
        return 1
    else:
        return 0

def de_queue():
    global front
    if(is_empty()):
        print("큐가 공백 상태입니다")
        return
    front += 1
    delete_data = queue[front]
    queue[front] = None
    print("삭제할 데이터: ", delete_data)

def print_queue():
    print("--현재 큐의 상태--")
    print("[", end= " ")
    for i in range(SIZE):
        print(queue[i], end = " ")
    print("]")
    print("front: ", front, "rear: ", rear)

print(queue); de_queue(); print(queue); de_queue(); print(queue); de_queue(); print(queue); de_queue();
