

def power(n, k, mod):
    """
    Return (n ** k) modulo mod.

    Complexity
    ----------
    O(log k)

    Examples
    --------
    >>> power(2, 10, 1000)
    24
    """
    if k == 0:
        return 1
    elif k % 2 == 1:
        return (n * power(n, k - 1, mod)) % mod
    else:
        return power(n ** 2, k // 2, mod)


if __name__ == '__main__':
    from doctest import testmod

    testmod()
