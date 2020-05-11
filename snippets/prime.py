

def is_prime(n):
    """
    Return if a number is a prime number.

    Complexity
    ----------
    O(n^{1/2})

    Examples
    --------
    >>> [is_prime(i) for i in range(1, 10)]
    [False, True, True, False, True, False, True, False, False]
    >>> is_prime(57)
    False
    >>> is_prime(10 ** 9 + 7)
    True
    """
    if n == 1:
        return False

    m = min(n - 1, int(pow(n, 1/2)) + 1)

    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True


def prime(n):
    """
    Return prime numbers <= n.

    Complexity
    ----------
    O(n)

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

    for i, isp in enumerate(is_prime):
        if isp:
            k = 2
            while k * i <= n:
                is_prime[k * i] = False
                k += 1

    return [i for i, isp in enumerate(is_prime) if isp]


if __name__ == '__main__':
    from doctest import testmod

    testmod()
