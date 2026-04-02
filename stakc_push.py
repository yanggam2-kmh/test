def isFull(stakc):
        if top>=len(stack)-1:
            return True
        return False

def push(data,stack):
    global top
    if isFull(stack):
        print("스택이 포화 상태입니다")
        return
    top += 1
    stack[top] = data

SIZE = 3
stack = [None for i in range(SIZE)]
global top
top = -1

print("--스택 상태--")
print(stack,top)
push('A',stack)
print(stack,top)
push('B',stack)
print(stack,top)
push('C',stack)
print(stack,top)
push('D',stack)
print(stack,top)

