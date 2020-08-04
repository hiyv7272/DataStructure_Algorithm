# Stack with list()


class Stack():
    def __init__(self):  # 생성자 초기화
        self.data = list()  # self.data list 구조로 초기화

    def isEmpty(self):  # 스택에 데이터 있는지 확인 func
        if len(self.data) == 0:  # self.data list에 데이터가 없다면
            return True  # True 리턴
        else:
            return False  # 초기값 False 리턴(self.data list에 데이터가 있다면)

    def push(self, value):  # 데이터 삽입 func
        self.data.append(value)  # self.data list에 데이터값을 넣음

    def pop(self):  # 데이터 삭제 func
        if len(self.data) == 0:  # self.data list에 데이터가 없다면
            print('Stack is Empty', -1)  # 스택이 비었음, -1 리턴
        else:
            data = self.data[-1]  # 마지막 데이터를 data 변수에 저장(self.data list에 데이터가 있다면)
            del self.data[-1]  # 마지막 데이터 삭제
            return data  # 삭제된 데이터 리턴

    def size(self):  # 데이터 갯수 확인 func
        return len(self.data)  # 스택의 데이터 길이 리턴

    def peek(self):  # 스택의 마지막 데이터 확인 func
        if self.data:  # 스택에 데이터가 있다면,
            return self.data[-1]  # 스택의 마지막 데이터 리턴
        else:
            print('Stack is Empty', -1)  # 스택이 비었음, -1 리턴

    def __repr__(self):  # 생성자 문자열 리턴 초기화
        return repr(self.data)  # 리턴하는 데이터는 문자열로 턴


if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())
    for i in range(4):
        stack.push(i)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())