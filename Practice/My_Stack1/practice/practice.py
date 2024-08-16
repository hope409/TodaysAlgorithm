stack = []

stack.append(1) # push(1)
stack.append(2) # push(2)
stack.append(3) # push(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())


stack_size = 10
stack2 = [0] * stack_size
top2 = -1

top2 += 1 # push(1)
stack2[top2] = 1
top2 += 1 # push(1)
stack2[top2] = 2
top2 += 1 # push(1)
stack2[top2] = 3

top2 -= 1 # pop()
print(stack2[top2 + 1])
print(stack2[top2]) # pop()
top2 -= 1
print(stack2[top2]) # pop()
top2 -= 1