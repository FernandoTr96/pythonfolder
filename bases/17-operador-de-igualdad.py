# Two different lists with the same values
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  → same values
print(a is b)   # False → different objects in memory

# Now make c point to the same object as a
c = a
print(a == c)   # True  → same values
print(a is c)   # True  → same object in memory
