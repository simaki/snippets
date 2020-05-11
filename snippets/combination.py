

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


class Combination:
    """
    Return Combination (n, k) modulo mod.

    Complexity
    ----------
    O(n) for Initialization, O(1) for call.

    Attributes
    ----------
    - f : list of int, length n + 1
        f = [i! modulo mod for i = 0, ..., n]
    - fi : list of int, length n + 1
        fi = [i!^-1 modulo mod for i = 0, ..., n]

    Examples
    --------
    >>> MOD = 10 ** 9 + 7
    >>> c = Combination(100, MOD)
    >>> c.f[:10]
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    >>> c(50)
    538992043
    """
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod

        self.f = self._get_f()
        self.fi = self._get_fi()

    def __call__(self, k):
        if not 0 <= k <= self.n:
            return 0
        else:
            num = self.f[self.n]
            deninv = (self.fi[k] * self.fi[self.n - k]) % self.mod
            return (num * deninv) % self.mod

    def _get_f(self):
        f = 1
        lf = [1]

        for i in range(1, self.n + 1):
            f = (f * i) % self.mod
            lf.append(f)

        return lf

    def _get_fi(self):
        ii = 1
        lii = [0, 1]  # [i^-1 modulo mod for i in 0, ..., n]
        fi = 1
        lfi = [1, 1]

        for i in range(2, self.n + 1):
            ii = (- lii[self.mod % i] * (self.mod // i)) % self.mod
            lii.append(ii)

            fi = (fi * ii) % self.mod
            lfi.append(fi)

        return lfi


if __name__ == '__main__':
    from doctest import testmod

    testmod()

