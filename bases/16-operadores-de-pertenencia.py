fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)       # True
print("mango" not in fruits)   # True


text = "Python is fun"

print("Python" in text)      # True
print("java" in text)        # False
print("Java" not in text)    # True  (case-sensitive)


person = {"name": "Alice", "age": 30}

print("name" in person)       # True (checks keys)
print("Alice" in person)      # False (values are not checked by default)
print("Alice" in person.values())  # True (explicitly check values)
