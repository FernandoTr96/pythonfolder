# Using curly braces
fruits = {"apple", "banana", "cherry"}

# Using set() constructor
numbers = {1, 2, 3, 3, 2}  # duplicates removed
print(numbers)  # {1, 2, 3}

fruits.add("orange")        # Add a single element
fruits.update(["mango", "grape"])  # Add multiple elements

fruits.remove("banana")     # Removes item (Error if not exists)
fruits.discard("banana")    # Removes item (No error if not exists)
fruits.pop()                # Removes and returns a random element
fruits.clear()              # Empty the set

for fruit in fruits:
    print(fruit)


a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(a | b)          # {1, 2, 3, 4, 5}
print(a.union(b))     # Same as above

# Intersection
print(a & b)          # {3}
print(a.intersection(b))

# Difference
print(a - b)          # {1, 2}
print(a.difference(b))

# Symmetric difference (elements not in both)
print(a ^ b)          # {1, 2, 4, 5}
print(a.symmetric_difference(b))

x = {1, 2}
y = {1, 2, 3}

print(x.issubset(y))   # True  (x is contained in y)
print(y.issuperset(x)) # True  (y contains all of x)
print(x.isdisjoint({4, 5})) # True (no common elements)

frozen = frozenset([1, 2, 3])
# frozen.add(4)  # ❌ Error: frozenset is immutable

# Squares from 0 to 4
squares = {x**2 for x in range(5)}
print(squares)  # {0, 1, 4, 9, 16}
