import sys
sys.stdin = open('input.txt')

li = [[0] * 4 for _ in range(4)]
g = [2, 3]
li.append(g)
print(li)
