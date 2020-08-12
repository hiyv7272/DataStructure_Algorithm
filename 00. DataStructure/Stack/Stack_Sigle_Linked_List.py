# Stack with Single Linked List
class Node(object):  # 싱글 링크드 리스트 노드 클래스
    def __init__(self, data):  # 생성자 초기화
        self.data = data  # 노드의 데이터 초기화 None
        self.next = None  # 노드의 다음노드정보는 None


class Stack(object):  # 스택 클래스
    def __init__(self):  # 생성자 초기화
        self.head = None  # 노드의 헤더정보는 초기값 None

    def isEmpty(self):  # 스택에 데이터 있는지 확인 func
        if self.head:  # 스택에 헤더가 있다
            return False  # 데이터가 있음으로, False 리턴
        else:
            return True  # (스택에 헤더가 없으면)데이터가 없음으로, True 리턴

    def push(self, data):  # 데이터 삽입 func
        new_node = Node(data)  # 새로운 객체 생성 및 새로운 노드로 저장
        new_node.next = self.head  # 새로운 노드의 다음노드정보는 헤더(즉, None)
        self.head = new_node  # 헤더는 새로운 노드

    def pop(self):  # 데이터 삭제 func
        if self.isEmpty():  # 스택에 데이터가 없다면
            print('Stack is Empty', -1)  # 스택이 비었음, -1 리턴
        else:  # 스택에 데이터가 있다면
            data = self.head.data  # 헤더의 데이터값을 data 변수에 저장
            self.head = self.head.next  # 헤더의 정보는 헤더의 다음노드정보
            return data  # 삭제될 data 변수 리턴

    def peek(self):  # 스택의 마지막 데이터 확인 func
        if self.isEmpty():  # 스택에 데이터가 없다면
            print('Stack is Empty', -1)  # 스택이 비었음, -1 리턴
        else:  # 스택에 데이터가 있다면,
            return self.head.data  # 스택 헤더의 데이터값을 리턴

    def size(self):  # 데이터 갯수 확인 func
        return len(self.data)  # 스택의 데이터 길이 리턴

    def _printList(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()


# 초기 test code
if __name__ == "__main__":
    stack = Stack()
    print('Stack is Empty?:', stack.isEmpty())
    print('Insert in Stack 0 to 10')
    for i in range(11):
        stack.push(i)

    print('Stack:')
    stack._printList()
    print('Stack peek:', stack.peek())
    for _ in range(5):
        print('Stack pop:', stack.pop())
    print('Stack:')
    stack._printList()