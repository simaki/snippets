

class UnionFind:
    """
    Union-find data structure.

    Parameters
    ----------
    - n : int
        Number of vertices.

    Complexity
    ----------
    O(log n)

    Examples
    --------
    >>> uf = UnionFind(4)
    >>> [uf.find(i) for i in uf.vertices]
    [0, 1, 2, 3]
    >>> [uf.size(i) for i in uf.vertices]
    [1, 1, 1, 1]
    >>> uf.union(0, 1)
    >>> [uf.find(i) for i in uf.vertices]
    [0, 0, 2, 3]
    >>> [uf.size(i) for i in uf.vertices]
    [2, 2, 1, 1]
    >>> uf.union(2, 3)
    >>> [uf.find(i) for i in uf.vertices]
    [0, 0, 2, 2]
    >>> [uf.size(i) for i in uf.vertices]
    [2, 2, 2, 2]
    >>> uf.union(0, 2)
    >>> [uf.find(i) for i in uf.vertices]
    [0, 0, 0, 0]
    >>> [uf.size(i) for i in uf.vertices]
    [4, 4, 4, 4]
    """
    def __init__(self, n):
        self.n = n

        self._find = {i: i for i in range(n)}
        self._size = {i: 1 for i in range(n)}

    @property
    def vertices(self):
        return range(self.n)

    def union(self, v0, v1):
        g0, g1 = self.find(v0), self.find(v1)
        g0, g1 = min(g0, g1), max(g1, g0)

        if g0 != g1:
            self._find[g1] = g0
            self._size[g0] += self._size[g1]

    def find(self, v):
        vertices = []

        while self._find[v] != v:
            v = self._find[v]
            vertices.append(v)

        for i in vertices:
            self._find[i] = v

        return v

    def size(self, v):
        return self._size[self.find(v)]


if __name__ == '__main__':
    from doctest import testmod

    testmod()
