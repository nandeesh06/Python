
# Function Arguments
# arguments vs parameter
def func(a,b):
    return a+b

func(10,20)
# here a,b are parameters they are local to func and 10, 20 are arguments

# Types of Function Arguments
# 1. Default Argument
#    A default argument is a parameter that assumes a default value if a value is not provided in the function call
#    for that argument.
#ex:
def myFun(x, y=50):
    print("x: ",x)
    print("y: ",y)

myFun(10)

# 2. Positional Arguments
# In positional arguments, values are assigned to parameters based on their order in the function call.
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

# 3. Keyword Arguments
# In keyword arguments, values are passed by explicitly specifying the parameter names, so the order doesn’t matter.
def student(fname, lname):
    print(fname, lname)
student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

# 4. Arbitrary Arguments
# In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments to a function
# using special symbols. There are two special symbols:
# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Nandeesh', last='KV')

