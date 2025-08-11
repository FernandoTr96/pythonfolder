# Empty list
my_list = []

# With elements
numbers = [1, 2, 3, 4]

# Mixed data types
mixed = [1, "hello", True, 3.5]

# Nested lists
nested = [[1, 2], [3, 4]]

# From another iterable
letters = list("hello")  # ['h', 'e', 'l', 'l', 'o']


# accessing elements
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple
print(fruits[-1])  # cherry (negative index = from end)

# slicing
print(fruits[0:2])  # ['apple', 'banana']
print(fruits[:2])   # ['apple', 'banana']
print(fruits[1:])   # ['banana', 'cherry']
print(fruits[::2])  # ['apple', 'cherry'] (step = 2)

# modify elements
fruits[1] = "blueberry"  # Change an element
print(fruits)  # ['apple', 'blueberry', 'cherry']

# add elements
fruits.append("orange")       # Add to end
fruits.insert(1, "mango")     # Insert at position
fruits.extend(["kiwi", "melon"])  # Add multiple
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]


# remove elements
fruits.remove("apple")   # Remove first occurrence
last = fruits.pop()      # Remove last (returns value)
item = fruits.pop(1)     # Remove at index
fruits.clear()           # Remove all

# search elements
print(numbers.index(20))      # First position of 20
print(numbers.count(20))      # Count occurrences
print(30 in numbers)          # True
print(40 not in numbers)      # True

# sort elements
nums = [4, 1, 3, 2]
nums.sort()         # Ascending
nums.sort(reverse=True)  # Descending
nums.reverse()      # Reverse order

# Without modifying original
sorted_nums = sorted(nums)

# copy lists
a = [1, 2, 3]
b = a.copy()      # Creates a new copy
c = list(a)       # Another way

# looping lists
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(i, fruit)


# useful
nums = [1, 2, 3]
print(len(nums))    # Length
print(sum(nums))    # Sum
print(max(nums))    # Largest
print(min(nums))    # Smallest

#unpacking
numbers = [1, 2, 3, 4, 5]
first, second, *rest = numbers
print(first)  # 1
print(second) # 2
print(rest)   # [3, 4, 5]

