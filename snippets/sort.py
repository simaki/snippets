import numpy as np


def bubble_sort(a):
    """
    Examples
    --------
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> arange = list(np.arange(100, dtype=int))
    >>> a = list(np.random.permutation(arange))
    >>> assert np.equal(bubble_sort(a), arange).all()
    """
    done = True
    for (i0, a0), a1 in zip(enumerate(a), a[1:]):
        if a0 > a1:
            a[i0], a[i0 + 1] = a1, a0
            done = False
    if done:
        return a
    else:
        return bubble_sort(a[:-1]) + a[-1:]


def quick_sort(a):
    """
    Examples
    --------
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> arange = np.arange(100, dtype=int)
    >>> a = np.random.permutation(arange)
    >>> assert np.equal(quick_sort(a), arange).all()
    """
    if len(a) == 0:
        return a
    else:
        m = a[0]
        al = [ai for ai in a if ai < m]
        ar = [ai for ai in a if ai > m]
        return quick_sort(al) + [m] + quick_sort(ar)


def selection_sort(a):
    """
    Examples
    --------
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> arange = np.arange(100, dtype=int)
    >>> a = np.random.permutation(arange)
    >>> assert (quick_sort(a) == arange).all()
    """
    if len(a) == 0:
        return a
    m = -(10 ** 10)
    mi = None
    for i, ai in enumerate(a):
        if m > ai:
            mi = i
            m = ai
    return a[mi] + selection_sort(a[:mi] + a[mi + 1 :])


def bogosort(a, seed=42):
    """
    Examples
    --------
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> arange = np.arange(5, dtype=int)
    >>> a = np.random.permutation(arange)
    >>> assert (bogosort(a) == arange).all()
    """
    np.random.seed(seed)

    done = False
    while not done:
        a = np.random.permutation(a)
        done = all(a0 < a1 for a0, a1 in zip(a, a[1:]))
    return a


if __name__ == "__main__":
    from doctest import testmod

    testmod()
