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


@validate_args
def my_function(x):
    return x


print(my_function(10))
print(my_function())
print(my_function(10,2))
print(my_function("hello"))
print(my_function(-1))