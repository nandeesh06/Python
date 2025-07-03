



# Generators

# Generators in Python are a powerful and memory-efficient way to create iterators.
# Instead of returning all values at once, generators yield items one at a time, only when requested.

# What is a Generator?
# A generator is a function funtion that uses the yield keyword instead of return.


# Ex:

nums = [7, 8, 9, 10]
it= iter(nums)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it))

class TopTen:

    def __init__(self):
        self.num =1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num +=1

            return val
        else:
            raise StopIteration

values = TopTen()

print(next(values))

for i in values:
    print(i)



