# Stack with Node
class Node(object):
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, data):
        self.head = Node(data, self.head)  # data = data, pointer = self.head
        self.count += 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.data
        else:
            print('Stack is Empty')

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.data
        else:
            print('Stack is Empty')

    def size(self):
        return self.count

    def __repr__(self):
        node = self.head
        data_list = list()
        while node:
            data_list.insert(0, node.data)
            node = node.pointer
        return repr(data_list)


# 초기 test code
if __name__ == "__main__":
    stack = Stack()
    print('Stack is Empty?:', stack.isEmpty())
    print('Insert in Stack 0 to 10')
    for i in range(11):
        stack.push(i)

    print('Stack:', stack)
    print('Stack peek:', stack.peek())
    for _ in range(5):
        print('Stack pop:', stack.pop())
    print('Stack:', stack)