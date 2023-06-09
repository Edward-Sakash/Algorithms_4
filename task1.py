"""Exercise(plot list vs. deque):
import timeit

def time_it(N):
setup_queue = f"from collections import deque; dq=deque(range({N}, 0, -1))"
fifo_queue = "dq.appendleft(None); dq.pop()"

queue_time = timeit.repeat(setup=setup_queue,
                        stmt= fifo_queue,
                        repeat=10,
                        number= 1000)

queue_mean = sum(queue_time) / len(queue_time)

setup_list = f"num = list(range({N}, 0, -1))" 
fifo_list = "num.append(None); num.pop(0)"

list_time = timeit.repeat(setup=setup_list,
                        stmt= fifo_list,
                        repeat = 3,
                        number = 1000)

list_mean = sum(list_time) / len(list_time)                        

return queue_mean, list_mean
X = [10, 100, 1000, 10000, 100000]
Y_queue = [time_it(num)[0] for num in X]
Y_list = [time_it(num)[1] for num in X]

plot Y_queue vs X
plot Y_list vs X
what is the time complexity of deques and list when we apply fifo-behaviour?"""

# Solution
import timeit
import matplotlib.pyplot as plt

def time_it(N):
    setup_queue = f"from collections import deque; dq=deque(range({N}, 0, -1))"
    fifo_queue = "dq.appendleft(None); dq.pop()"

    queue_time = timeit.repeat(setup=setup_queue,
                               stmt=fifo_queue,
                               repeat=10,
                               number=1000)

    queue_mean = sum(queue_time) / len(queue_time)

    setup_list = f"num = list(range({N}, 0, -1))" 
    fifo_list = "num.append(None); num.pop(0)"

    list_time = timeit.repeat(setup=setup_list,
                              stmt=fifo_list,
                              repeat=3,
                              number=1000)

    list_mean = sum(list_time) / len(list_time)

    return queue_mean, list_mean


X = [10, 100, 1000, 10000, 100000]
#X = range(10, 10000)
#X = [num for num in X if num % 4 == 0]

Y_queue = [time_it(num)[0] for num in X]
Y_list = [time_it(num)[1] for num in X]

# Plotting Y_queue vs X
plt.plot(X, Y_queue, label='deque')
plt.xlabel('N')
plt.ylabel('Time (seconds)')
plt.title('deque FIFO Behavior')
plt.legend()
plt.show()

# Plotting Y_list vs X
plt.plot(X, Y_list, label='list')
plt.xlabel('N')
plt.ylabel('Time (seconds)')
plt.title('List FIFO Behavior')
plt.legend()
plt.show()

"""The time complexity of deques and lists when applying FIFO
 (First-In-First-Out) behavior is as follows:
Deques:
'deque.appendleft(item)': This operation adds an item
to the left end of the deque. The time complexity of this
operation is O(1) since deques are optimized for efficient
insertion and deletion at both ends.
deque.pop(): This operation removes an item from the right end
of the deque. The time complexity of this operation is also O(1)
since it involves removing an element from the end of the deque.
Therefore, the time complexity of deque operations in a FIFO
manner is O(1), as they both operate on the ends of the deque.

Lists:
'list.append(item)': This operation adds an item to the right end
of the list. The amortized time complexity of this operation is O(1)
since appending to the end of a list is typically fast due to dynamic
array resizing.
'list.pop(0)': This operation removes the first item from the list,
which requires shifting all other elements down by one position.
The time complexity of this operation is O(N), where N is the length
of the list, as it involves moving all subsequent elements.
Therefore, when applying FIFO behavior with lists, the time complexity
of list.append() is O(1), while the time complexity of list.pop(0) is O(N).
In summary, deques maintain a constant time complexity of O(1) for both
appending and popping at both ends, making them more efficient for FIFO
operations compared to lists, which have a linear time complexity of O(N)
for popping from the front.
"""

# put two diagrams together