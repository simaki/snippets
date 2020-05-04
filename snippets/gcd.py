

def gcd(a, b):
    """
    Return the greatest common divisor of two numbers.

    Complexity
    ----------
    log(max(a, b))

    Examples
    --------
    >>> gcd(6, 10)
    2
    >>> gcd(1, 6)
    1
    """
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Return the least common multiplier of two numbers.

    Complexity
    ----------
    log(max(a, b))

    Examples
    --------
    >>> lcm(6, 10)
    30
    >>> lcm(1, 6)
    6
    """
    return a * b // gcd(a, b)


if __name__ == '__main__':
    from doctest import testmod

    testmod()
