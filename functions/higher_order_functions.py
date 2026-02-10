

""" Higher order functions
    A function that takes a function as a parameter and/or returns a functions as it's return value"""

# Ex: sorted, filter , map


# map
# syntax: map(func, *iterable)
# map function will return an iterator that calculates the functions applied to each element of iterables


# example
l =[2,3,4]
def sqr(x):
    return x**2
print(list(map(sqr,l)))

l1 = [10,11,12]
l2 = [13,14,15]
print(list(map(lambda x, y: x+y,l1,l2)))
