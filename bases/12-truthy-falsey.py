# Truthy values
if "Hello":
    print("'Hello' is truthy")

if [1, 2, 3]:
    print("[1, 2, 3] is truthy")

# Falsy values
if "":
    print("Empty string is truthy")  # This won't run
else:
    print("Empty string is falsy")

if 0:
    print("0 is truthy")  # This won't run
else:
    print("0 is falsy")

if None:
    print("None is truthy")  # This won't run
else:
    print("None is falsy")
