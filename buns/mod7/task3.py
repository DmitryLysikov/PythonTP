import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


def memoize(func):
    cache = {}
    func_name = func.__name__
    func_doc = func.__doc__

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.__name__ = func_name
    wrapper.__doc__ = func_doc
    return wrapper


def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        if len(args) > 1:
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(*args)
    return wrapper


@memoize
@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


@validate_args
def fibonacci_no_memoize(n):
    if n < 2:
        return n
    return fibonacci_no_memoize(n-1) + fibonacci_no_memoize(n-2)


new_fib = timer(fibonacci)
new_fib_nomem = timer(fibonacci_no_memoize)

print(new_fib(12))
print(new_fib_nomem(12))