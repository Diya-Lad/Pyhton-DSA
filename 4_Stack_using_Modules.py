# 1: Collections --> deque
import collections

stack = collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

stack.pop()
print(stack)

import queue

stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)

print(stack)

print(stack.get())

stack = queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40, timeout=1)

# To get the msg use timeouts




