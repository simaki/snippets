from heapq import heappush, heappop
import numpy as np


def bubble_sort(a):
    """
    Complexity
    ----------
    O(n^2)

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
    Complexity
    ----------
    O(n log n)

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


def comb_sort(a):
    """
    Complexity
    ----------
    O(n log n)

    Examples
    --------
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> arange = np.arange(100, dtype=int)
    >>> a = np.random.permutation(arange)
    >>> assert np.equal(comb_sort(a), arange).all()
    """
    h = len(a)
    while h > 1:
        h = int(h / 1.3)
        for (i0, a0), a1 in zip(enumerate(a), a[h:]):
            if a0 > a1:
                a[i0], a[i0 + h] = a1, a0
    done = False
    while not done:
        done = True
        for (i0, a0), a1 in zip(enumerate(a), a[1:]):
            if a0 > a1:
                a[i0], a[i0 + 1] = a1, a0
                done = False
    return a


def merge_sort(a):
    """
    Examples
    --------
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> arange = list(np.arange(100, dtype=int))
    >>> a = list(np.random.permutation(arange))
    >>> assert np.equal(merge_sort(a), arange).all()
    """
    n = len(a)

    if n <= 1:
        return a

    al = merge_sort(a[: n // 2])
    ar = merge_sort(a[n // 2 :])

    il, ir = 0, 0
    b = []
    while il < len(al) or ir < len(ar):
        if il >= len(al):
            b.append(ar[ir])
            ir += 1
        elif ir >= len(ar):
            b.append(al[il])
            il += 1
        elif al[il] < ar[ir]:
            b.append(al[il])
            il += 1
        else:
            b.append(ar[ir])
            ir += 1

    return b


def heap_sort(a):
    """
    Examples
    --------
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> arange = np.arange(100, dtype=int)
    >>> a = np.random.permutation(arange)
    >>> assert (heap_sort(a) == arange).all()
    """
    heap = []
    for ai in a:
        heappush(heap, ai)
    return [heappop(heap) for _ in a]


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


def shell_sort(a):
    pass  # TODO


def library_sort(a):
    pass  # TODO


def library_sort(a):
    pass  # TODO


def insertion_sort(a):
    pass  # TODO


def shaker_sort(a):
    pass  # TODO


def norm_sort(a):
    pass  # TODO


# def odd_even_sort(a, odd=False):
#     """
#     Examples
#     --------
#     >>> import numpy as np
#     >>> np.random.seed(42)
#     >>> arange = np.arange(5, dtype=int)
#     >>> a = np.random.permutation(arange)
#     >>> odd_even_sort(a)
#     >>> assert (odd_even_sort(a) == arange).all()
#     """
#     done = True
#     for i in range()
#         if a[2 * i] > a[2 * (i + 1)]:
#             a[2 * i], a[2 * (i + 1)] = a[2 * (i + 1)], a[2 * i]


#     # for (i, a0), a1 in zip(enumerate(a[int(odd) :: 2]), a[int(odd) + 2 :: 2]):
#     #     print(a0, a1)
#     #     if a0 > a1:
#     #         a[2 * i + int(odd)], a[2 * (i + 1) + int(odd)] = a1, a0
#     #         done = False
#     return odd_even_sort(a, odd=not odd)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
