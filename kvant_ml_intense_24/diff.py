def use(func):
    func("alim")
    print('used it')

def greeting(name):
    print("Hello, " + name + '!')

use(greeting)