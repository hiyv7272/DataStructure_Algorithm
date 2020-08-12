# Stack with Node
class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head) # value = item, pointer = self.head
        self.count += 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print('Stack is Empty')

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print('Stack is Empty')

    def size(self):
        return self.count

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
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