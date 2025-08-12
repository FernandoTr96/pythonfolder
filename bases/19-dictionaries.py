# Simple dictionary
person = {
    "name": "Fernando",
    "age": 28,
    "city": "Cuernavaca"
}
print(person)

#Access values
print(person["name"])     # Fernando
print(person.get("age"))  # 28

#Modify values
person["age"] = 29
person["city"] = "Monterrey"

#Add new key-value pairs
person["profession"] = "Developer"

#Remove elements
person.pop("age")        # Remove by key
person.popitem()         # Remove the last inserted pair
del person["city"]       # Another way
person.clear()           # Empty the dictionary

#loop
person = {"name": "Fernando", "age": 28, "city": "Cuernavaca"}

# Only keys
for key in person:
    print(key)

# Keys and values
for key, value in person.items():
    print(key, value)

# Only values
for value in person.values():
    print(value)

#check if key exist
if "name" in person:
    print("Key 'name' exists")

#nested
employees = {
    "dev1": {"name": "Fernando", "role": "Backend"},
    "dev2": {"name": "Ana", "role": "Frontend"}
}
print(employees["dev1"]["role"])  # Backend

#compreension
# Create a dict with squares of numbers
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# useful
person.keys()     # dict_keys(['name', 'age', 'city'])
person.values()   # dict_values(['Fernando', 28, 'Cuernavaca'])
person.items()    # dict_items([('name', 'Fernando'), ('age', 28), ('city', 'Cuernavaca')])
