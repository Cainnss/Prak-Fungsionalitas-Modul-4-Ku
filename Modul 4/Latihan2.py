# decorator uppercase_decorator
def uppercase_decorator(function):
    def wrapper():
        func_result = function()
        return func_result.upper()
    return wrapper

# Memakai decorator @uppercase_decorator untuk mendekorasi fungsi say_hi
@uppercase_decorator
def say_hi():
    return 'hello there'

result = say_hi()
print(result)