# boj_11279.py
# 최대 힙
"""
최대 힙 구현 문제

굳이 선언해서 이렇게 해야하나
그냥 완전 이진 트리겠다

일단 리스트 가장 끝에 넣고
부모랑 비교(last // 2)가 부모니까.
부모보다 크면 부모랑 자리 바꾸고
이거 반복하면 되는거 아닌감
"""
import sys
input = sys.stdin.readline
N = int(input())
heap = [0]
last = 0
for work in range(N):
    order = int(input())
    # 들어온 값이 0이면(최대값을 뺴라는 오더라면)
    if order == 0:
        # 길이가 0이면 0 출력
        if len(heap) == 1:
            print(0)
        # 길이가 1이였다면 그냥 빼고 출력
        elif len(heap) == 2:
            print(heap.pop())
            last -= 1
        # 길이가 1 초과일 경우들
        else:
            # 말단에 있는 놈을 빼서 루트에 넣고
            print(heap[1])
            heap[1] = heap.pop()
            last -= 1
            # 왼쪽 오른쪽 비교해서 더 큰놈이랑 교환을 계속
            s_parent = 1
            while True:
                left = s_parent * 2
                right = s_parent * 2 + 1
                max_idx = s_parent
                # 왼,오가 있는지 확인하고, 있으면 max_idx 갱신 시도
                if last >= left:
                    if heap[max_idx] < heap[left]:
                        max_idx = left
                if last >= right:
                    if heap[max_idx] < heap[right]:
                        max_idx = right
                # 부모가 더 크면 갱신 x while 깨고 나가기
                if max_idx == s_parent:
                    break
                # 부모가 더 작으면 교환하고 계속 수행
                else:
                    heap[s_parent], heap[max_idx] = heap[max_idx], heap[s_parent]
                    s_parent = max_idx
    else:
        # 힙이 비어 있으면
        if len(heap) == 1:
            heap.append(order)
            last += 1
        # 힙에 값이 있으면
        else:
            # 일단 맨 끝에 넣고
            heap.append(order)
            last += 1
            # 부모랑 비교. 언제까지? 루트에 도달할 때 까지.
            start = last
            while start != 1:
                p_idx = start // 2
                # 새로 들어온 것이 부모보다 크면 교환
                if heap[p_idx] < heap[start]:
                    heap[p_idx], heap[start] = heap[start], heap[p_idx]
                    start = p_idx
                else:
                    break
