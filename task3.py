"""refactor previous code so that you can call merge_sort with a function as an argument. By default mergesort should sort by list element.
print(merge_sort([2,5,1,3,4])) --->[1, 2, 3, 4, 5]

print(merge_sort(dictionaries, key=lambda item: item['city'])) ----->
[{'name': 'Grace', 'age': 29, 'city': 'Boston'}, {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}, {'name': 'Henry', 'age': 31, 'city': 'Dallas'}, {'name': 'Jack', 'age': 33, 'city': 'Denver'}, {'name': 'David', 'age': 28, 'city': 'Houston'}, {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}, {'name': 'Ivy', 'age': 26, 'city': 'Miami'}, {'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Emma', 'age': 27, 'city': 'San Francisco'}, {'name': 'Frank', 'age': 32, 'city': 'Seattle'}]

print(merge_sort(dictionaries, key=lambda item: item['name']))--->
[{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}, {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}, {'name': 'David', 'age': 28, 'city': 'Houston'}, {'name': 'Emma', 'age': 27, 'city': 'San Francisco'}, {'name': 'Frank', 'age': 32, 'city': 'Seattle'}, {'name': 'Grace', 'age': 29, 'city': 'Boston'}, {'name': 'Henry', 'age': 31, 'city': 'Dallas'}, {'name': 'Ivy', 'age': 26, 'city': 'Miami'}, {'name': 'Jack', 'age': 33, 'city': 'Denver'}]

print(merge_sort(dictionaries, key=lambda item: item['age']))--->
[{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Ivy', 'age': 26, 'city': 'Miami'}, {'name': 'Emma', 'age': 27, 'city': 'San Francisco'}, {'name': 'David', 'age': 28, 'city': 'Houston'}, {'name': 'Grace', 'age': 29, 'city': 'Boston'}, {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}, {'name': 'Henry', 'age': 31, 'city': 'Dallas'}, {'name': 'Frank', 'age': 32, 'city': 'Seattle'}, {'name': 'Jack', 'age': 33, 'city': 'Denver'}, {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}]"""


# Solution

print("_______________________________________________")
#######################################################

################################################################

def merge_sort(arr, key=None):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key=key)
    right = merge_sort(arr[mid:], key=key)

    return merge(left, right, key=key)


def merge(left, right, key=None):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key is not None:
            if key(left[i]) <= key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


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

output = merge_sort([2, 5, 1, 3, 4])
print("merge_sort([2, 5, 1, 3, 4]):", end=" ")
for item in output:
    print(item, end=" ")

output = merge_sort(dictionaries, key=lambda item: item['city'])
print("\nmerge_sort(dictionaries, key=lambda item: item['city']):")
for item in output:
    print(item)

output = merge_sort(dictionaries, key=lambda item: item['name'])
print("\nmerge_sort(dictionaries, key=lambda item: item['name']):")
for item in output:
    print(item)

output = merge_sort(dictionaries, key=lambda item: item['age'])
print("\nmerge_sort(dictionaries, key=lambda item: item['age']):")
for item in output:
    print(item)

print(merge_sort([2,5,1,3,4])) #--->[1, 2, 3, 4, 5]