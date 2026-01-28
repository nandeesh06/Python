
"""What are decorator?
    Decorator is function which is used modify or add extra work for another function without changing its source
    code."""

def dec_function(fn):
    print("I'm outer function")
    def inner():
        print("I'm inside inner function and will execute first")
        fn()
        print("After running function")
    return inner

def actual_function():
    print("I'm the actual function")

# calling the actual_function with decorator
actual_function = dec_function(actual_function)
actual_function()

# We can use @ symbol to simplify the above method
@dec_function
def actual_function():
    print("I'm the actual function")

# and just call the actual function
actual_function()


