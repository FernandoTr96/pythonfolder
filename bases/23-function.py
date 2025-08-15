# standard function
def greet():
    print("Hello, world!")

greet()  # Calling the function


# function that returns a value
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7


# parameters and arguments
def multiply(x, y):   # x, y = parameters
    return x * y

print(multiply(2, 5)) # 2, 5 = arguments


# Default parameters
def greet(name="Guest"):
    print(f"Hello {name}!")

greet()                  # Hello Guest!  (default)
greet("Fernando")        # Hello Fernando!

# Keyword arguments
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce(age=25, name="Luis")  # order swapped but works


# Doc string
def square(n):
    """Returns the square of a number."""
    return n ** 2
print(square.__doc__)  # Returns the square of a number.


# Collect parameters into a tuple
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10


# Collect parameters as dictionary
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show_info(name="Ana", age=30)
# name = Ana
# age = 30


# Scopes
x = "global"  # Global scope

def outer():
    x = "enclosing"  # Enclosing scope

    def inner():
        x = "local"  # Local scope
        print(x)     # local
    inner()

outer()


# nonlocal
def outer():
    x = "outer value"

    def inner():
        nonlocal x
        x = "modified by inner"
    inner()
    print(x)

outer()
# Output: modified by inner



