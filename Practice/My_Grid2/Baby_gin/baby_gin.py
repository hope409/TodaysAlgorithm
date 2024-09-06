import sys
sys.stdin = open('sample_input.txt')

def find_triplet(arr):
    for i in range(10):
        if arr[i] >= 3:
            arr[i] = arr[i] - 3
            return True
    return False

def find_run(arr):
    for i in range(8):
        if arr[i] >= 1 and arr[i + 1] >= 1 and arr[i + 2] >= 1:
            arr[i] -= 1
            arr[i + 1] -= 1
            arr[i + 2] -= 1
            return True
    return False

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    # 인덱스 : 짝수 - 플레이어1 / 홀수 - 플레이어2
    card_info = list(map(int, input().split()))
    player1 = [0] * 10 # 플레이어1의 카드리스트
    player2 = [0] * 10 # 플레이어2의 카드리스트
    turn = 0 # 몇번재 턴인지
    while turn < 12:
        turn += 1
        if turn % 2: # 플레이어1의 차례
            player1[card_info.pop(0)] += 1
            if turn >= 5:
                if find_triplet(player1) or find_run(player1): # 체크
                    print(f"#{test_case} 1")
                    break
        else: # 플레이어2의 차례
            player2[card_info.pop(0)] += 1
            if turn >= 6:
                if find_triplet(player2) or find_run(player2): # 체크
                    print(f"#{test_case} 2")
                    break
    else: # 무승부
        print(f"#{test_case} 0")
