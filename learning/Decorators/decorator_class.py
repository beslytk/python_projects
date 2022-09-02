# Decorators

# decorator class

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Executed Before', self.original_function.__name__)
        result = self.original_function(*args, **kwargs)
        print('Executed After', self.original_function.__name__, '\n')    
        return result

@decorator_class
def display_info_c(name, age):
    print('display_info_c ran with arguments ({}, {})'.format(name, age))

display_info_c('Tom', 25)
display_info_c('Hardy', 30)