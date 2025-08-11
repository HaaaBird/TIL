# swea_1248
# 공통 조상 찾기

def find_parents(parents, A, B):
    # 부모 찾는 함수
    # 1 - 최 정점까지 올라가면서 부모 리스트 모두 append
    # 2 - 이후 겹치는 부모 있으면 break
    # parents -> idx 테이블. 자식 idx 에 부모 번호를 값으로 매핑걸어둔거.
    # A를 통해서 찾는 순서 -> A부모를 parents 에서 찾음: parents[A] -> 나온 값이 부모
    # 나온 값이 1이면? if parents[A] == 1: break
    # else: visit.append(parents[A])
    # now_node = parents[A]

    visits = []
    # A의 맨 위까지 경로를 찾아보자
    now_node = A
    while now_node != 1:
        now_node = parents[now_node]
        visits.append(now_node)
    # B 의 경로를 찾으며 공통 부분 찾기
    now_node = B
    while True:
        now_node = parents[now_node]
        if now_node in visits:
            return now_node

def count_all_node(children, start_node):
    size = 1
    for child in children[start_node]:
        size += count_all_node(children, child)
    return size


T = int(input())
for case in range(1, T + 1):
    V, E, A, B = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = [0] * (V + 1)
    children = {i:[] for i in range(1, V+1)}
    for i in range(0,len(arr),2):
        p = arr[i]
        c = arr[i+1]
        parents[c] = p
        children[p].append(c)
    a_parents = find_parents(parents, A, B)
    size = count_all_node(children, a_parents)
    print(1)