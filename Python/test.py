# Stack DFS



tree_map = {
    1: [2,3],
    2: [4,5],
    3: [6],
    4: [],
    5: [7],
    6: [],
    7: []
}


stack = []
visit = []
location = 1
while True:
    if len(tree_map[location]) == 0:
        location = stack.pop()
    for i in range(len(tree_map[location])):
        if tree_map[location][i] not in visit:
            stack.append(location)
            location = tree_map[location][i]
            break
    if tree_map[1] not in a:
        pass
