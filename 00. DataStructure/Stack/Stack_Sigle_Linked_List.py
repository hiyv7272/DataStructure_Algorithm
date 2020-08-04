# Stack with Single Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            print ('Stack is Empty', -1)
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def peek(self):
        if self.isEmpty():
            print ('Stack is Empty', -1)
        else:
            return self.head.data

    def size(self):
        return len(self.data)


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
