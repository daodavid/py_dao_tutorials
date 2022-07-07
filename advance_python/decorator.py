"""

A decorator is a function that takes another function as an argument
and extends its behavior without changing the original function explicitly.
"""


def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


def currency(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)

    return wrapper


