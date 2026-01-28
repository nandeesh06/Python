"""Why do we use from functools import wraps in decorators?
  When you decorate a function without using @wraps, Python loses the original function’s metadata
  (name, docstring, annotations, etc.).
  - functools.wraps copies metadata from the original function to the wrapper function.
  What is “metadata”?

  Function metadata includes:
  __name__
  __doc__
  __module__
  __annotations__
  help()
  Used by debuggers, loggers, frameworks (pytest, flask, fastapi)"""

# Problem without wraps
def my_decorator(fn):
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        fn(*args,**kwargs)
    return wrapper

@my_decorator
def add(a,b):
    """Adds two numbers"""
    return a+b

print(add.__name__)
print(add.__doc__)
help(add)


from functools import wraps
def my_decorator(fn):
    wraps(fn)
    def wrapper(*args,**kwargs):
        """Wrapper function"""
        fn(*args, **kwargs)
    return wrapper

@my_decorator
def add(a,b):
    """adds two numbers"""
    return a+b

print(add.__name__)
print(add.__doc__)
help(add)


# Why this matters in real project?
# Ex 1: Logging
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args,**kwargs)
    return wrapper

# here without wraps, logs will say :
# Calling wrapper

"""Pytest uses function names and docstrings for:
Test discovery
Reporting
Markers
❌ Without wraps → pytest may show wrong test names
✅ With wraps → correct test reporting"""