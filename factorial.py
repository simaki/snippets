

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
        return power((n ** 2) % mod, k // 2, mod)


def factorial(n, mod):
    """
    Return n! modulo mod (a prime number).

    Complexity
    ----------
    O(n)

    Examples
    --------
    >>> MOD = 10 ** 9 + 7
    >>> factorial(100, MOD)
    437918130
    """
    f = 1
    for i in range(1, n + 1):
        f *= i
        f %= mod
    return f


def combination(n, k, mod):
    """
    Return Combination (n, k) modulo mod.

    Complexity
    ----------
    O(n + log(mod))

    Examples
    --------
    >>> MOD = 10 ** 9 + 7
    >>> combination(100, 50, MOD)
    538992043
    """
    d = (factorial(k, mod) * factorial(n - k, mod)) % mod
    dinv = power(d, mod - 2, mod)
    return (factorial(n, mod) * dinv) % mod


if __name__ == '__main__':
    from doctest import testmod

    testmod()

