try:
    number = int("abc")  # This will raise ValueError
except ValueError:
    print("That’s not a valid number!")

try:
    x = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print(f"Error occurred: {e}")


try:
    num = int("42")
except ValueError:
    print("Invalid number")
else:
    print(f"Number is {num}")  # Runs only if no error
finally:
    print("Execution finished")  # Always runs


class NegativeNumberError(Exception):
    """Raised when a number is negative."""
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Number cannot be negative")
    print("Number is positive")

try:
    check_positive(-5)
except NegativeNumberError as e:
    print("Custom error:", e)
