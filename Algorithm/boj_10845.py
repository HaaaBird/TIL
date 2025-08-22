# boj_10845.py
# 큐

"""
정수를 저장하는 큐를 구현한 다음,
입력으로 주어지는 명령을 처리하는
프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""


import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None          # 추가: 꼬리 포인터
        self.my_len = 0

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node      # 첫 노드가 곧 tail
        else:
            # O(1) 추가
            self.tail.next = node
            self.tail = node
        self.my_len += 1

    def front(self):
        if self.head is None:     # 빈 큐 가드
            return -1
        return self.head.data

    def back(self):
        if self.head is None:     # 빈 큐 가드
            return -1
        return self.tail.data     # tail 사용

    def size(self):
        return self.my_len

    def empty(self):
        return 1 if self.head is None else 0

    def pop(self):
        if self.head is None:
            return -1
        result = self.head.data
        self.head = self.head.next
        self.my_len -= 1
        if self.head is None:     # 비게 되었으면 tail도 초기화
            self.tail = None
        return result


if __name__ == "__main__":
    input = sys.stdin.readline              # I/O 가속 (권장)
    N = int(input())
    my_queue = Queue()
    for _ in range(N):
        order = input().split()
        if order[0] == "push":
            my_queue.push(order[1])
        elif order[0] == "pop":
            print(my_queue.pop())
        elif order[0] == "size":
            print(my_queue.size())
        elif order[0] == "empty":
            print(my_queue.empty())
        elif order[0] == "front":
            print(my_queue.front())
        elif order[0] == "back":
            print(my_queue.back())
