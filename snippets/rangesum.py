from itertools import accumulate


class RangeSum:
    """
    Examples
    --------
    >>> rs = RangeSum([1, 10, 100, 1000, 10000])
    >>> rs(2, 5)
    11100
    """
    def __init__(self, a):
        self.a = a
        self.cumsum = [0] + list(accumulate(a))

    def __call__(self, il, ir):
        return self.cumsum[ir] - self.cumsum[il]


if __name__ == '__main__':
    from doctest import testmod

    testmod()

