import functools
from random import randint


def maybe(func):
    """Use as a coin flip for a decorated function to execute"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        num = randint(0, 1)
        if num == 0:
            return func(*args, **kwargs)
        else:
            return

    return wrapper
