# Task 1
# Exercise(plot list vs. deque):
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
what is the time complexity of deques and list when we apply fifo-behaviour?

# Task 2
# Exercise(sort list of dictionaries):

dictionaries = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 28, "city": "Houston"},
    {"name": "Emma", "age": 27, "city": "San Francisco"},
    {"name": "Frank", "age": 32, "city": "Seattle"},
    {"name": "Grace", "age": 29, "city": "Boston"},
    {"name": "Henry", "age": 31, "city": "Dallas"},
    {"name": "Ivy", "age": 26, "city": "Miami"},
    {"name": "Jack", "age": 33, "city": "Denver"}
]

print(merge_sort(dictionaries))

change the merge_sort so that you can sort by age.

# Task 3
# Exercise(sort list of dictionaries III):
refactor previous code so that you can call merge_sort with a function as an argument.  By default mergesort should sort by list element.
print(merge_sort([2,5,1,3,4])) --->[1, 2, 3, 4, 5]

print(merge_sort(dictionaries, key=lambda item: item['city'])) ----->
[{'name': 'Grace', 'age': 29, 'city': 'Boston'}, {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}, {'name': 'Henry', 'age': 31, 'city': 'Dallas'}, {'name': 'Jack', 'age': 33, 'city': 'Denver'}, {'name': 'David', 'age': 28, 'city': 'Houston'}, {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}, {'name': 'Ivy', 'age': 26, 'city': 'Miami'}, {'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Emma', 'age': 27, 'city': 'San Francisco'}, {'name': 'Frank', 'age': 32, 'city': 'Seattle'}]

print(merge_sort(dictionaries, key=lambda item: item['name']))--->
[{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}, {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}, {'name': 'David', 'age': 28, 'city': 'Houston'}, {'name': 'Emma', 'age': 27, 'city': 'San Francisco'}, {'name': 'Frank', 'age': 32, 'city': 'Seattle'}, {'name': 'Grace', 'age': 29, 'city': 'Boston'}, {'name': 'Henry', 'age': 31, 'city': 'Dallas'}, {'name': 'Ivy', 'age': 26, 'city': 'Miami'}, {'name': 'Jack', 'age': 33, 'city': 'Denver'}]

print(merge_sort(dictionaries, key=lambda item: item['age']))--->
[{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Ivy', 'age': 26, 'city': 'Miami'}, {'name': 'Emma', 'age': 27, 'city': 'San Francisco'}, {'name': 'David', 'age': 28, 'city': 'Houston'}, {'name': 'Grace', 'age': 29, 'city': 'Boston'}, {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}, {'name': 'Henry', 'age': 31, 'city': 'Dallas'}, {'name': 'Frank', 'age': 32, 'city': 'Seattle'}, {'name': 'Jack', 'age': 33, 'city': 'Denver'}, {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}]

# Task 4
# Exercise(Palindrome Checker):
Write a function that checks whether a given string is a palindrome or not using a deque.
Hint:
use the popleft() und pop() methods

print(is_palindrome("radar"))   # True
print(is_palindrome("python"))  # False
print(is_palindrome("madam"))   # True

# Task 5
# Exercise(Reverse a Sentence):
Write a function that takes a sentence as input and uses a deque to reverse the words in the sentence.

# Test the function
print(reverse_sentence("Hello, world!"))  # world! Hello,
print(reverse_sentence("Python is fun"))  # fun is Python
print(reverse_sentence("I love coding"))  # coding love I

# Task 6
# Exercise(Balanced Parentheses)
Write a function that checks whether a given string of parentheses is balanced or not using a deque.
# Test the function
the output should be in this format
print(is_balanced_parentheses("()"))           # True
print(is_balanced_parentheses("({[]})"))       # True
print(is_balanced_parentheses("({[]}))"))      # False
print(is_balanced_parentheses("({[}])"))       # False