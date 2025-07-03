
# Raw String
# ----------------
# A raw string completely ignores all escape characters
# Ex:
print(r'That is Carol\'s cat.')
# output: That is Carol\'s cat.

# Useful String Methods
# -----------------------
str ="NANDEESH"
print(str.lower())
# output: nandeesh
print(str.upper())
# output: NANDEESH
print(str.isalpha())
# output: True
print(str.isalnum())
# output: Ture
print(str.isnumeric())
# output: False
print(str.title())
# output: Nandeesh
print(str.startswith("NA"))
# output: True
print(str.endswith("SH"))
# output: True

# The join() and split() String Methods
# --------------------------------------------------
# The join() method is useful when you have a list of strings that need to be joined together into a single string
# value. The join() method is called on a string, gets passed a list of strings, and returns a string
# Ex1:
str_lst = ['cats', 'rats', 'bats']
new_str = " ".join(str_lst)
print(new_str)
# output: cats rats bats

# Ex2:
new_str2 = ' '.join(['My', 'name', 'is', 'Simon'])
print(new_str2)
# output = My name is Simon

# join() is called on a string value and is passed a list value.
# (It’s easy to accidentally call it the other way around.) The split() method does the opposite: It’s called on a
# string value and returns a list of strings
# Ex1:
input_str = "My name is Simon"
list_of_string = input_str.split(" ")
print(list_of_string)
# output: ['My', 'name', 'is', 'Simon']

# Ex2:
input_str1 = "My, name, is, Simon"
list_of_string2 = input_str1.split(", ")
print(list_of_string2)
# output: ['My', 'name', 'is', 'Simon']

# Justifying Text with rjust(), ljust(), and center()
# ---------------------------------------------------------
# The rjust() and ljust() string methods return a padded version of the string they are called on,
# with spaces inserted to justify the text. The first argument to both methods is an integer length for the justified string
# str.rjust(num, char)
print('Hello'.rjust(10, "-"))
# output : "    Hellow"

print('Hello'.ljust(10))
# output: "Hello    "

print("Hello".center(15,"-"))
# output: "     Hello     "


# Removing Whitespace with strip(), rstrip(), and lstrip()
# -----------------------------------------------------------
# Sometimes you may want to strip off whitespace characters (space, tab,and newline) from the left side, right side,
# or both sides of a string. The strip() string method will return a new string without any whitespace characters at the
# beginning or end. The lstrip() and rstrip() methods will remove whitespace characters from the left and right ends, respectively
# Ex:
spam = "   Hello World   "
print(spam.strip())
# output: "Hello World"

print(spam.lstrip())
# output: "Hello World   "

print(spam.rsplit())
# output: "    Hello World"
