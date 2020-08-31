# Queue with List
class Queue(object):
    def __init__(self):
        self.items = list()

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print('Queue is Empty')

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print('Queue is Empty')

    def size(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)


# 초기 test code
if __name__ == "__main__":
    queue = Queue()
    print('Queue is Empty?:', queue.isEmpty())
    print('Insert in Queue 0 to 10')
    for i in range(11):
        queue.enqueue(i)
    print('Queue :', queue)
    print('Queue peek:', queue.peek())
    for _ in range(5):
        print('Queue pop:', queue.dequeue())
    print('Queue :', queue)
