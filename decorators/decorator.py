


def outer(fn):

    def inner(*args, **kwargs):
        print("Decorating the add function")
        fn(*args,**kwargs)
        print("Decoration Completed")
    return inner

def add(a,b):
    """ add function which add two numbers"""
    return a+b



add = outer(add)
add(1,2)


print(add.__name__)
print(help(add))

