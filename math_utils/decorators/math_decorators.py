def only_int_float_func(func):
    def wrapper(*args, **kwargs):
        if (not all(isinstance(arg, int) or isinstance(arg, float) for arg in args)
                or not all(isinstance(arg, int) or isinstance(arg, float) for arg in kwargs.values())):
            raise TypeError('only int or float arguments are allowed')

        return func(*args, **kwargs)

    return wrapper
