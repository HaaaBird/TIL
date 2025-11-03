# boj_5639.py
"""

전위순회한 값이 넘어온다.
이걸 후위순회 하게 한다.


생각 나는건 일단 그래프에 담는다?
이진 탐색 트리를 일단 구현을 해 봐야 하나? 시간이 맞을련지

"""

import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self, data):
        # 처음에 생성할땐 이렇게. 자기가 뿌리이자 마지막
        self.root = Node(data)

    def insert(self, data):
        self.current_node = self.root
        while True:
            if data < self.current_node.data:  # 마지막 노드 값이 더 크다
                if self.current_node.left is None:
                    self.current_node.left = Node(data)
                    self.current_node.left.parent = self.current_node
                    break
                else:
                    self.current_node = self.current_node.left
            else:
                if self.current_node.right is None:
                    self.current_node.right = Node(data)
                    self.current_node.right.parent = self.current_node
                    break
                else:
                    self.current_node = self.current_node.right

    def postorder(self):
        now_node = self.root
        visit = set()
        while len(visit) != len(nums):
            if now_node.left is not None and now_node.left.data not in visit:
                now_node = now_node.left
                continue
            elif now_node.right is not None and now_node.right.data not in visit:
                now_node = now_node.right
                continue
            else:
                print(now_node.data)
                visit.add(now_node.data)
                now_node = now_node.parent


if __name__ == "__main__":
    nums = []
    while True:
        try:
            n = int(input())
            nums.append(n)
        except:
            break
    b_tree = BST(nums[0])
    for i in range(1, len(nums)):
        b_tree.insert(nums[i])
    b_tree.postorder()
