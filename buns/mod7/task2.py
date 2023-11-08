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

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(12))
