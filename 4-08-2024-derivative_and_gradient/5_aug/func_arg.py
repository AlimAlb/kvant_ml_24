
def diff(f, x):
    pass

def print_hello(name):
    s = "hello, " + name
    print(s)

def call(f, name):
    print('Calling func')
    f(name)
    print('End')

call(print_hello, 'Alim')