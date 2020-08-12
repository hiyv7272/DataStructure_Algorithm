# Queue with Two Stacks
class Queue(object):
    def __init__(self):
        self.in_stack = list()
        self.out_stack = list()

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def isEmpty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            print('Queue is Empty')

    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        else:
            print('Queue is Empty')

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return repr(self.out_stack)
        else:
            print('Queue is Empty')


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