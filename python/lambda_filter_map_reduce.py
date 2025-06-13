from functools import reduce
# A lambda function in Python is a small anonymous function (i.e., a function without a name) defined using the lambda keyword.
# It's mainly used for short, throwaway functions, especially in combination with functions like map(), filter(), and sorted()

# Basic Syntax
# lambda arguments : expression
# Ex:
add = lambda x,y: x+y
print(add(2,3))

# map
# syntax: map(function, iterables)
# Applies a function to every item in the iterable and returns a new iterator.
square = list(map(lambda x:x**2,range(1,5)))
print(square)

# filter
# syntax: filter(function, iterables)
# Filters items in the iterable by applying a function that returns True or False
str_list = ["name_pwc","age","town_pwc"]
filtered_list =list(filter(lambda x: "_pwc" in x,str_list))
print(filtered_list)

# reduce
# syntax: reduce(function, iterables)
# Applies a function cumulatively to the items of an iterable.
summing = reduce(lambda x,y: x+y, range(5))
print(summing)

# Interview quesions
# 1. Convert List of Strings to Uppercase
names = ['alice', 'bob', 'charlie']
uppercase= list(map(lambda name:name.upper(), names))
print(uppercase)

# 2. Find Maximum Using reduce()
#    Use reduce() to find the maximum number in a list.
nums = [3, 6, 2, 8, 4]
max_value= reduce(lambda x,y: x if x>y else y, nums)
print(max_value)

# 3. Remove Empty Strings
words = ["hello", "", "world", "", "python"]
filter_words= list(filter(lambda word: "" != word, words))
print(filter_words)

# 4. Get All Palindromes from List of Strings
words = ['madam', 'racecar', 'apple', 'noon', 'python']
palindrome_list = list(filter(lambda x: x==x[::-1], words))
print(palindrome_list)

# 5. Double the Even Numbers Only
nums = [1, 2, 3, 4, 5, 6]
doubled = list (map(lambda y: y * 2, filter(lambda x: x % 2 == 0,nums)))
print(doubled)

# 6. Square all odd numbers in a list
nums = [1, 2, 3, 4, 5, 6]
odd_doubled = list(map(lambda y: y * 2,filter(lambda x: x % 2 != 0, nums)))

# 7. Capitalize names that start with 'a'
names = ['alice', 'bob', 'adam', 'charlie']
cap_list = list(map(lambda x: x.capitalize(), filter(lambda x: x.startswith("a"), names)))
print(cap_list)

# 8. Reverse each string in a list using map()
words = ['apple', 'banana', 'car']
rev_words = list(map(lambda word: word[::-1], words))
print(rev_words)

# 9. From a list of tuples (name, score), get names of those who scored above 70
data = [('Alice', 85), ('Bob', 67), ('Charlie', 90)]
names = tuple(map(lambda x: x[0],filter(lambda x: x[1] >= 70, data)))
print(names)