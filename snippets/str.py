def z_algorithm(s):
    """
    Return lengths of longest common prefixes.

    Examples
    --------
    >>> z_algorithm('abcbcba')
    [7, 0, 0, 0, 0, 0, 1]
    >>> z_algorithm('aaabaaaab')
    [9, 2, 1, 0, 3, 4, 2, 1, 0]
    >>> z_algorithm('mississippi')
    [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> z_algorithm('ababacaca')
    [9, 0, 3, 0, 1, 0, 1, 0, 1]
    >>> z_algorithm('aaaaa')
    [5, 4, 3, 2, 1]
    """
    z = [0] * len(s)
    z[0] = len(s)

    i0 = 1
    llcp = 0

    while i0 < len(s):
        while i0 + llcp < len(s) and s[llcp] == s[i0 + llcp]:
            llcp += 1
        z[i0] = llcp

        if llcp == 0:
            i0 += 1
        else:
            i1 = 1
            while i0 + i1 < len(s) and i1 + z[i1] < llcp:
                z[i0 + i1] = z[i1]
                i1 += 1

            i0 += i1
            llcp -= i1

    return z


if __name__ == "__main__":
    from doctest import testmod

    testmod()
