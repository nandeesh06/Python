

# Positional and Keyword Arguments
#Positional Arguments a=1, b=2, c=3
def funct1(a,b,c):
    print(a,b,c)

funct1(1,2,3)


def funct2(a,b,c=10):
    print(a,b,c)

#both will work and for c takes default value
funct2(2,3,4)
funct2(2,3)


def funct3(*args,**kwargs):
    print(args,kwargs)

funct3("name","age","town", name="nandeesh", age=27, town="mycoity")



# Iterables
# Packed Value: any  iterable can be considered a packed value
# unpacking Sets and Dictionaries
d= {"key":1, "Key2":2, "Key3":3}
d2={**d,**d}
print(d2)

# for e in d  --> e iterates through the keys : "key1", "key2", "key3"
# so, when unpacking d, we are actually unpacking the keys of d

a,b,c=d  # -> a= "key1", b= "key2", c="key3"
         # -> a= "key2", b= "key1", c="key3"
         # -> a= "key3", b= "key2", c="Key1"
         # etc...
# Dictionaries(and Sets) are unordered types
# They can be iterated, but there is no guarantee the order of the results will match your results


# Using with ordered type

a, *b= [-10,1,2,3,4]
print(a,b)
# a = -10, b = [1, 2, 3, 4]
a,*b = "xyz"
print(a, b)
