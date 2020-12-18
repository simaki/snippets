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


def _with_dummy(s, dummy):
    out = s[0]
    for c in s[1:]:
        out += dummy + c
    return out


def manacher(s):
    """
    >>> manacher("abcbcba")
    [1, 0, 1, 0, 3, 0, 7, 0, 3, 0, 1, 0, 1]
    >>> manacher("mississippi")
    [1, 0, 1, 0, 1, 4, 1, 0, 7, 0, 1, 4, 1, 0, 1, 0, 1, 4, 1, 0, 1]
    >>> manacher("ababacaca")
    [1, 0, 3, 0, 5, 0, 3, 0, 1, 0, 3, 0, 5, 0, 3, 0, 1]
    >>> manacher("aaaaa")
    [1, 2, 3, 4, 5, 4, 3, 2, 1]
    """
    dummy = "*"
    assert dummy not in s

    s = _with_dummy(s, dummy)

    n = len(s)
    len_pals = [None] * n

    i = 0
    j = 0
    while i < n:
        while (0 <= i - j) and (i + j < n) and s[i - j] == s[i + j]:
            j += 1
        len_pals[i] = j

        k = 1
        while (0 <= i - k) and (i + j < n) and (k + len_pals[i - k] < j):
            len_pals[i + k] = len_pals[i - k]
            k += 1

        i += k
        j = 0

    palindromes = [s[i - j + 1 : i + j] for i, j in enumerate(len_pals)]
    palindromes = [p.replace(dummy, "") for p in palindromes]
    len_pals = [len(p) for p in palindromes]

    return len_pals


def longest_palindrome(s):
    """
    >>> longest_palindrome("abcbcba")
    'abcbcba'
    >>> longest_palindrome("mississippi")
    'ississi'
    >>> longest_palindrome("ababacaca")
    'acaca'
    >>> longest_palindrome("aaaaa")
    'aaaaa'
    """
    dummy = "*"
    assert dummy not in s

    s = _with_dummy(s, dummy)

    n = len(s)
    len_pals = [None] * n

    i = 0
    j = 0
    while i < n:
        while (0 <= i - j) and (i + j < n) and s[i - j] == s[i + j]:
            j += 1
        len_pals[i] = j

        k = 1
        while (0 <= i - k) and (i + j < n) and (k + len_pals[i - k] < j):
            len_pals[i + k] = len_pals[i - k]
            k += 1

        i += k
        j = 0

    palindromes = [s[i - j + 1 : i + j] for i, j in enumerate(len_pals)]
    palindromes = [p.replace(dummy, "") for p in palindromes]
    longest = max((len(p), p) for p in palindromes)[1]

    return longest





if __name__ == "__main__":
    from doctest import testmod

    testmod()
