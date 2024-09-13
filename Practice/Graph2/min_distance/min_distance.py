import sys
sys.stdin = open('sample_input.txt')

def distance_move(end, start = 0, distance = 0):
    global min_distance
    if start == end:
        if min_distance is None or distance < min_distance:
            min_distance = distance
        return

    if min_distance is not None and distance >= min_distance:
        return

    for next in adj_li[start]:
        if next is not None:
            distance_move(end, next, distance + adj_li[start][next])


t = int(input())
for test_case in range(1, t + 1):
    node, edge = map(int, input().split())
    adj_li = [{} for _ in range(node + 1)]
    for _ in range(edge):
        start, end, length = map(int, input().split())
        adj_li[start][end] = length
    min_distance = None
    distance_move(node)
    print(f"#{test_case} {min_distance}")