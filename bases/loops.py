# for loop

fruits = ["apple", "pear", "graves"]

for fruit in fruits:
    print(fruit)

# iterables
# String (iterable of characters)
for ch in "Hello":
    print(ch)

# Set (unordered)
for n in {3, 1, 2}:
    print(n)

# Dictionary iterates over keys
person = {"name": "Fer", "age": 26}
for key in person:
    print(key, "=>", person[key])

# 0,1,2,3,4
for i in range(5):
    print(i)

# 2,4,6,8
for i in range(2, 10, 2):
    print(i)

# 5,4,3,2,1
for i in range(5, 0, -1):
    print(i)


# while loop
counter = 0
while counter < 3:
    print("counter =", counter)
    counter += 1


# break continue and pass
for n in range(1, 6):
    if n == 3:
        continue      # skip number 3
    if n == 5:
        break         # stop loop at 5
    print(n)          # prints 1, 2, 4

def todo_later():
    pass  # to be implemented later


# iterate nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Access
print(matrix[1][2])  # 6

# Loop through rows and columns
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# Flatten using list comprehension
flat = [x for row in matrix for x in row]
print(flat)  # [1,2,3,4,5,6,7,8,9]


# Nested dictionaries

employees = {
    101: {"name": "Ana", "role": "Dev", "skills": ["Python", "SQL"]},
    102: {"name": "Luis", "role": "QA",  "skills": ["Selenium"]},
}

# Safe access with get
print(employees.get(101, {}).get("name"))

# Loop through keys and sub-keys
for emp_id, data in employees.items():
    name = data["name"]
    skills = ", ".join(data["skills"])
    print(f"{emp_id}: {name} ({skills})")

# Update nested value
employees[101]["skills"].append("Airflow")
