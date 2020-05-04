

def prime_factorization(n):
    """
    Perform prime factorization of a number.

    Complexity
    ----------
    O(n)

    Examples
    --------
    >>> prime_factorization(1)
    {}
    >>> prime_factorization(2)
    {2: 1}
    >>> prime_factorization(12)
    {2: 2, 3: 1}
    >>> prime_factorization(57)
    {3: 1, 19: 1}
    """
    pmax = int(n ** 0.5 // 1) + 1

    factors = {}
    for p in range(2, pmax + 1):
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    if n != 1:
        factors[n] = factors.get(n, 0) + 1

    return factors


if __name__ == '__main__':
    from doctest import testmod

    testmod()
