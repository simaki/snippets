def split(iterable, size=10 ** 4):
    """
    Split iterable into N chunks and yield them.

    Parameters
    ----------
    - iterable : iterable
        Iterable to split.
    - size : int, default 10 ** 4
        Maximum length of each chunk.

    Examples
    --------
    >>> iterable = [i for i in range(10)]
    >>> for chunk in split(iterable, size=3):
    ...     print(chunk)
    [0, 1, 2]
    [3, 4, 5]
    [6, 7, 8]
    [9]
    """
    n = -(-len(iterable) // size)

    for i in range(n):
        if i != n - 1:
            yield iterable[i * size:(i + 1) * size]
        else:
            yield iterable[i * size:]


def main():
    iterable = [i for i in range(10)]
    for chunk in split(iterable, size=3):
        print(chunk)


if __name__ == '__main__':
    main()
