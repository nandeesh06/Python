
# Iterators
# ------------
"""An iterator is an object that can be looped through one item at a time using next().
 Any object with __iter__() and __next__() methods is an iterator"""
#Ex:
nums = [10,20,30]
it_nums = iter(nums) # this makes an iterator
print(next(it_nums))
# 10
print(next(it_nums))
# 20
print(next(it_nums))
# 30

# Generators
# -------------
"""Generators in Python are a powerful and memory-efficient way to create iterators. Instead of returning all values at 
once, generators yield items one at a time, only when requested.
What is a Generator?
A generator is a function that uses the yield keyword instead of return."""

def even_numbers(n):
    for i in range(n):
        if i%2 == 0:
            yield i

for i in even_numbers(10):
    print(i)



