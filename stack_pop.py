def isEmpty(stack):
    if top == -1:
        return True
    else:
        return False

def pop(stack):
    global top
    if isEmpty(stack):
        print("스택이 공백상태입니다.")
        return

    data = stack[top]
    stack[top] = None
    top -= 1
    return data

stack=['A','B','C']
global top
top = 2

print("-- 스택상태 --")
print(stack,top)
pop(stack)
print(stack,top)
pop(stack)
print(stack,top)
pop(stack)
print(stack,top)
pop(stack)
print(stack,top)
