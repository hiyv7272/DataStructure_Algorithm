# Queue with Linked_List
class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            print('Queue is Empty')

    def peek(self):
        return self.head.value

    def size(self):
        return self.count

    def print(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
        print()
        # print('here!!!!!',self.head)
        # if self.head:
        #     queue_list = list()
        #     for value in self.head:
        #         queue_list.append(value)
        #     return queue_list
        # else:
        #     print('Queue is Empty')


# 초기 test code
if __name__ == "__main__":
    queue = Queue()
    print('Queue is Empty?:', queue.isEmpty())
    print('Insert in Queue 0 to 10')
    for i in range(11):
        queue.enqueue(i)

    print('Queue size: ', queue.size())
    print('Queue :', queue.print())
    print('Queue peek:', queue.peek())
    for _ in range(5):
        print('Queue pop:', queue.dequeue())
    print('Queue size: ', queue.size())
    print('Queue :', queue.print())