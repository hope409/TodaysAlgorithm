'''
mirkovC4nizCC44
C4
'''
### 시간초과
def main():
    string = input()
    bomb_string = input()
    while bomb_string in string:
        string = string.replace(bomb_string, "").strip()    
    if string:
        print(string)
    else:
        print("FRULA")
    
### 스택을 사용해서 시간 단축
def main2():    
    string = input()
    bomb_string = input()
    stack = []
    bomb_len = len(bomb_string)

    for char in string:
        stack.append(char)
        # 스택의 마지막 부분이 bomb_string과 같다면 pop
        if ''.join(stack[-bomb_len:]) == bomb_string:
            del stack[-bomb_len:]

    # 스택이 비어있다면 "FRULA"를 출력하고, 그렇지 않으면 결과를 출력
    result = ''.join(stack)
    if result:
        print(result)
    else:
        print("FRULA")
