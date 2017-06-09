from dump1 import dump


@dump
def double(*args, **kwargs):
    "Returns all arguments doubled"
    output_list = [2 * arg for arg in args]
    output_dict = {k:2*v for k, v in kwargs.items()}
    return output_list, output_dict
