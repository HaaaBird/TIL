# boj_1927.py
# 최소 힙

import sys

input = sys.stdin.readline


def insert_data(data):
    global heap, last
    heap.append(data)
    last += 1
    p_idx = last // 2
    n_end = last
    while p_idx != 0:
        # 부모가 자식보다 크다면
        if heap[p_idx] > heap[n_end]:
            # 위치 교환
            heap[p_idx], heap[n_end] = heap[n_end], heap[p_idx]
            # 인덱스 갱신
            n_end = p_idx
            p_idx = n_end // 2
        else:
            break


def delete_data():
    global heap, last
    # 가장 먼저 할 것은 머리 꺼내기
    # 들어있는게 없으면
    if len(heap) == 1:
        print(0)
    # 들어있는게 있으면
    elif len(heap) == 2:
        print(heap[1])
        heap.pop()
        last -= 1
    else:
        # 출력 먼저 하고 마지막 요소랑 자리 바꾸기
        print(heap[1])
        heap[1] = heap.pop()
        last -= 1
        min_idx = 1
        s_idx = 1
        while True:
            # 왼쪽이 있으면
            if min_idx * 2 <= last:
                if heap[min_idx * 2] < heap[min_idx]:
                    min_idx = min_idx * 2
            if s_idx * 2 + 1 <= last:
                if heap[s_idx * 2 + 1] < heap[min_idx]:
                    min_idx = s_idx * 2 + 1
            if s_idx == min_idx:
                break
            else:
                heap[s_idx], heap[min_idx] = heap[min_idx], heap[s_idx]
                s_idx = min_idx


N = int(input())
heap = [0]
last = 0

for _ in range(N):
    work = int(input())
    if work == 0:
        delete_data()
    else:
        insert_data(work)
