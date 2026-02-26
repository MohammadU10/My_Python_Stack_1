
def hello_func1():
    return 'Hello Function.'


def hello_func2(greeting):
    if len(greeting) > 20:
        raise ValueError('Your greeting length is too long. Max length: 20 characters.')
    return '{} Function.'.format(greeting)
