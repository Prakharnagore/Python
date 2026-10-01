from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")
else:
    print("not empty")
print(queue)

# FIFO (First In First Out) data structure.
# Why deque - because it is faster than list for append and pop operations.
