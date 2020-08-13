# Deque
from .Queue import Queue


class Deque(Queue):
    def enqueue_back(self, data):
        self.datas.append(data)

    def dequeue(self):
        data = self.datas.pop(0)
        if data is not None:
            return data
        else:
            print('Deque is Empty')


# 초기 test code
if __name__ == "__name__":
    deque = Deque()
    print('Deque is Empty?:', deque.isEmpty())
    print('Insert in Deque 0 to 10')
    for i in range(11):
        deque.enqueue(i)

    print('Deque size: ', deque.size())
    print('Deque :', deque)
    print('Deque peek:', deque.peek())
    for _ in range(5):
        print('Deque pop:', deque.dequeue_front())

    print('Deque size: ', deque.size())
    print('Deque :', deque)

    print('Insert in Deque enqueu_back(50)')
    deque.enqueue_back(50)
    print('Deque peek:', deque.peek())
    print('Deque :', deque)
