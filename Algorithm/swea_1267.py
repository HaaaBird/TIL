# swea_1267.py
# 작업 순서


T = 10
for case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = [[] for _ in range(V)]
    children = [[] for _ in range(V)]
    finish_work = set()
    result = []

    for i in range(0, len(arr), 2):
        num1, num2 = arr[i] - 1, arr[i + 1] - 1
        parents[num2].append(num1)
        children[num1].append(num2)

    while len(result) != V:
        for i in range(V):
            if i not in finish_work:
                stack = [i]
                while stack:
                    now = stack.pop()
                    if now in finish_work:
                        continue
                    can_do = True
                    for p in parents[now]:
                        if p not in finish_work:
                            can_do = False
                            break
                    if can_do:  # 부모 전부 완료된 경우
                        result.append(now + 1)
                        finish_work.add(now)

                        for child in children[now]:
                            if child not in finish_work:
                                # 자식도 부모 완료 확인
                                can_child = True
                                for p in parents[child]:
                                    if p not in finish_work:
                                        can_child = False
                                        break
                                if can_child:
                                    stack.append(child)

    print(f"#{case} {' '.join(map(str, result))}")



