# swea_16293.py
# 그래프 경로


"""
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

V 가 노드의 수, E 가 간선의 수인데, V 가 크지 않으니 방향성 그래프를 카운트 리스트 형태로 구현한다. idx 에 리스트를 넣는다.
# dfs 는 stack과 visit 을 이용해서 방문을 확인하는 코드니까
# 일단 시작 stack 에 시작점을 넣는다.
# while 에 진입하고, stack 머리를 pop 한다.
# 만약, visits 에 pop 한 요소가 없으면 visits 에 넣는다.
# 그리고 자식 값을 가져와서 stack 에 역순으로 넣는다.
# 만약 now가 target에 도달했으면 return 1
# 그렇지 않으면 while 조건 자체를 stack 가 비었을 때 깨지게 하고 return 0
"""

def DFS(tree, S, G):
    stack = [S]
    visits = set()

    while len(stack) != 0:
        now = stack.pop()
        if now == G:
            return 1
        if now not in visits:
            visits.add(now)
            child = tree[now]
            if len(child) != 0:
                for ch in range(len(child)-1, -1, -1):
                    stack.append(child[ch])
    return 0

T = int(input())
for case in range(1, T + 1):
    V, E = map(int, input().split()) # 노드의 수, 간선의 수
    edge_matrix = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int,input().split()) # 시작위치 도착위치

    tree = [[] for _ in range(V + 1)]
    for info in edge_matrix:
        tree[info[0]].append(info[1])

    result = DFS(tree, S, G)
    print(f"#{case} {result}")