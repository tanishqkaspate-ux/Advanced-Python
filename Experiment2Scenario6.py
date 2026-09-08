from datetime import datetime
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Function: {func.__name__}")
        print(f"Input: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"Output: {result}")
        print("-" * 40)

        return result

    return wrapper


@logger
def add(a, b):
    return a + b


@logger
def multiply(a, b):
    return a * b


@logger
def greet(name):
    return f"Hello, {name}!"


# Function calls
result1 = add(10, 20)
result2 = multiply(5, 6)
result3 = greet("Tanishq")

print("Results:")
print(result1)
print(result2)
print(result3)
