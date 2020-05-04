

def prime(n):
    """
    Return prime numbers <= n.

    Examples
    --------
    >>> prime(1)
    []
    >>> prime(2)
    [2]
    >>> prime(10)
    [2, 3, 5, 7]
    """
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False

    for i, p in enumerate(is_prime):
        if p:
            k = 2
            while k * i <= n:
                is_prime[k * i] = False
                k += 1

    return [i for i, p in enumerate(is_prime) if p]


if __name__ == '__main__':
    from doctest import testmod

    testmod()
