"""Exercise(sort list of dictionaries):
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

change the merge_sort so that you can sort by age."""

# Solution

def merge_sort(arr, key="age"):
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
            if left[i][key] <= right[j][key]:
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

sorted_by_age = merge_sort(dictionaries)

# Determine the maximum lengths for each column
max_name_length = max(len(d["name"]) for d in sorted_by_age)
max_age_length = max(len(str(d["age"])) for d in sorted_by_age)
max_city_length = max(len(d["city"]) for d in sorted_by_age)

# Print the sorted list in columns
for d in sorted_by_age:
    print(f"{{:<{max_name_length}}} {{:<{max_age_length}}} {{:<{max_city_length}}}".format(
        d["name"], d["age"], d["city"]
    ))


