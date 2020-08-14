# Deque collections
from collections import deque

# 초기 test code
if __name__ == "__name__":
    # dq = deque(maxlen=4)  ## 길이 조절 가

    dq = deque([])
    print('Insert in Deque 0 to 10')
    for i in range(11):
        dq.append(i)

    print('Deque: ', dq)

    print('Deque popleft: ', dq.popleft())
    print('Deque pop: ', dq.pop())
    print('Deque appendleft 0', dq.append(0))

    print('Deque: ', dq)
