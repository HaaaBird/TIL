# 연결 리스트
- 구성요소
  - 노드: 데이터를 보관하는 필드
  - 포인터: 다음 데이터를 나타내는 것
  - 헤드: 링크드 리스트의 첫 번째 요소
- 링크드 리스트의 종류
  - 단일 링크드 리스트: 각 노드에 다음 요소를 가리키는 포인터만 있는 경우
  - 이중 링크드 리스트: 각 노드에 다음 요소를 가리키는 포인터와 이전 요소를 가리키는 포인터가 모두 있는 경우.
  - 환형 링크드 리스트: 마지막 노드가 헤드를 가리켜 내선순환 열차를 만드는 링크드 리스트
- 링크드 리스트의 성능
  - 노드를 선형 탐색함으로 O(n), 추가나 제거 에선 O(1) 이게 가장 강점
- 링크드 리스트 파이썬에서 만들기
```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        if not self.head: # 링크드 리스트에 첫 요소가 들어온 것이라면, 
            self.head = Node(data) # 새로운 Node 만들어서 head 에 할당
            return # 종료
        current = self.head # 첫 요소가 아니라면 머리로 이동
        while current.next: # current.next != None 임. None이 나오면 While 깸. 
            current = current.next # 계속해서 다음으로 이동.
        current.next = Node(data) 
        # While 깨고 나온다면, next가 없는 currnent 에 도달했다면 해당 Node 의 next에 새로운 node 생성 후 next 에 할당.

    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return "End"

    def search(self, target):
        current = self.head
        while current.next != None:
            if current.data == target:
                return True
            else:
                current = current.next
        return False
    
    def remove(self, target):
        # 타겟이 헤드면
        if self.head == target:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data ==

```

- 링크드 리스트가 가져야 할 속성
  - Node: 머리에 해당하는 부분.
    - data = 값에 해당하는 부분
    - next: 방향, 혹은 순서가 있는 경우에 다음을 가리킴
  - Linked List: 위에서 선언한 Node들을 담을 객체로 쓸 것을 클래스로 선언한 것
    - head: 리스트의 정점, 머리
    - append(): 요소 추가하는 함수. while 통해서 current 를 갱신하며 Next 가 없는 요소 찾아서 할당. 
    - __str__(): 매직메서드 이용해서 리스트 전체를 출력하는 함수 구성하는 것.
    - 