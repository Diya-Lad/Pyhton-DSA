# 1st way
import collections

q = collections.deque()
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)

q.pop()
print(q)

# Another way popleft and append method

# 2nd way

import queue

q = queue.Queue()
q.put(10)
q.put(20)
q.put(30)

print(q)

print(q.get())

# put(item, block = true/false, timeout)
# put_nowait(item)

# get( block = true/false, timeout = none)
# get_nowait()

