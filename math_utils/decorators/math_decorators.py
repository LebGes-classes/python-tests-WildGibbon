def only_int_float_func(func):
    def wrapper(*args, **kwargs):
        if (any(not isinstance(arg, int) for arg in args) or
                any(not isinstance(kwarg, int) for kwarg in kwargs.values())):
            if (any(not isinstance(arg, float) for arg in args) or
                    any(not isinstance(kwarg, float) for kwarg in kwargs.values())):
                raise TypeError('only int or float arguments are allowed')

        return func(*args, **kwargs)

    return wrapper
