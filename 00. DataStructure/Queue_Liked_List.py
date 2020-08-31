# Queue with Linked_List
class Node(object):
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def enqueue(self, data):
        node = Node(data)
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
            data = self.head.data
            self.head = self.head.pointer
            self.count -= 1
            return data
        else:
            print('Queue is Empty')

    def peek(self):
        return self.head.data

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
    queue = Queue()
    print('Queue is Empty?:', queue.isEmpty())
    print('Insert in Queue 0 to 10')
    for i in range(11):
        queue.enqueue(i)

    print('Queue size: ', queue.size())
    print('Queue :', queue)
    print('Queue peek:', queue.peek())
    for _ in range(5):
        print('Queue pop:', queue.dequeue())
    print('Queue size: ', queue.size())
    print('Queue :', queue)