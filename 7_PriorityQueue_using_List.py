# q = []
# q.append(10)
# q.append(40)
# q.sort()
# q.append(20)
# q.sort()

# q.pop(0)
# q.pop(0)

import queue

q = queue.PriorityQueue()
q.put(10)
q.put(50)
q.put(40)
q.put(10)
q.put(20)

print(q.get())
print(q.get())

# To set priority by own
q = []
q.append((1,"diya"))
q.append((5,"diya"))
q.append((6,"shruti"))
q.append((4,"vaibhavi"))

q.sort(reverse=True) # Sort in reverse
print(q)

q.pop(0)
print(q)



