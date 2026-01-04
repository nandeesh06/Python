
"""
Free Variables
-----------------
A free variable is a variable referenced in a function that is neither local to that function nor global,
but comes from an enclosing scope and is preserved by a closure.

Closure
--------
A closure is a function object that remembers and has access to variables from its enclosing (outer) scope,
even after the outer function has finished executing
"""

def outer():
    x= "Python"
    def inner():
        print(x)
    return inner

f = outer()
f()


print(f.__code__.co_freevars)
print(f.__closure__)


"""
Python cells and Multi Scoped Variables
----------------------------------------
In the above the value of "x" share between two scopes:
    1. outer
    2. inner
the label "x" is in two different scopes but always reference the same "value".
 
                    ----------------                     ---------------
    outer.x  ---->  | cell  OxA500 |                     | str OxFF100 |
                    |              |   ------------>     |             | 
    inner.x ----->  |      OxFF100 |                     |      Python | 
                    ----------------                     ---------------
"""


