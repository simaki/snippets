from abc import ABCMeta, abstractmethod
from math import log2


class SegmentTree(metaclass=ABCMeta):
    """
    Parameters
    ----------
    - array : list
        Input array to evaluate range statistics.

    Attributes
    ----------
    - a : array
        Extended array with length 2 ** k.
    - n_a : int
        Length of the array.
    - n_t : int
        Length of the tree.
    - tree : list
        Segment tree.
    - section : list of (int, int)
        Section of each vertex.
    """
    def __init__(self, array):
        self.array = array

        self.a = self.__get_a()
        self.n_a = len(self.a)
        self.n_t = 2 * self.n_a - 1
        self.tree = self.__get_tree()
        self.section = self.__get_section()

    def parent(self, v):
        return (v - 1) // 2

    def childs(self, v):
        return (2 * v + 1, 2 * v + 2)

    def leaf(self, i):
        return i + self.n_a - 1

    def __get_a(self):
        n = 2 ** (int(log2(len(self.array))) + 1)
        return self.array + [
            self.default() for _ in range(n - len(self.array))
        ]

    def __get_tree(self):
        tree = [self.default() for _ in range(self.n_t)]

        for i_tree in range(self.n_t - 1, -1, -1):
            if i_tree >= self.n_a - 1:
                tree[i_tree] = self.a[i_tree - self.n_a + 1]
            else:
                c0, c1 = self.childs(i_tree)
                tree[i_tree] = self.stat([tree[c0], tree[c1]])

        return tree

    def __get_section(self):
        section = [None for _ in range(self.n_t)]

        for i_tree in range(self.n_t - 1, -1, -1):
            if i_tree >= self.n_a - 1:
                i = i_tree - self.n_a + 1
                section[i_tree] = (i, i + 1)
            else:
                c0, c1 = self.childs(i_tree)
                section[i_tree] = (section[c0][0], section[c1][1])

        return section

    def __call__(self, il, ir, v=0):
        sl, sr = self.section[v]
        if (ir <= sl) or (il >= sr):
            return self.default()
        elif il <= sl and sr <= ir:
            return self.tree[v]
        else:
            c0, c1 = self.childs(v)
            return self.stat([self(il, ir, c0), self(il, ir, c1)])

    @abstractmethod
    def stat(self, iterable):
        """
        Statistics value of an iterable.
        """

    @property
    @abstractmethod
    def default(self):
        """
        The default value satisfying `stat([default, x]) = x` for any x.
        """

    @abstractmethod
    def update(self, i, a, v=None):
        """
        Update and return self.
        """
        return self


class SegmentTreeMin(SegmentTree):
    """
    Examples
    --------
    >>> array = [5, 3, 7, 9, 1, 4, 6, 2]
    >>> st = SegmentTreeMin(array)
    >>> st.tree
    [1, 3, 1, 3, 7, 1, 2, 5, 3, 7, 9, 1, 4, 6, 2]
    >>> st.min(0, 1)
    5
    >>> st.min(0, 7)
    1
    >>> st.update(0, 2).tree
    [1, 2, 1, 2, 7, 1, 2, 2, 3, 7, 9, 1, 4, 6, 2]
    """
    def stat(self, iterable):
        return min(iterable)

    def default(self):
        return float('inf')

    def update(self, i, a, v=None):
        if v is None:
            v = self.leaf(i)

        self.tree[v] = self.stat([self.tree[v], a])

        if v != 0:
            return self.update(i, a, v=self.parent(v))


class SegmentTreeMax(SegmentTree):

    def stat(self, iterable):
        return max(iterable)

    def default(self):
        return -float('inf')

    def update(self, i, a, v=None):
        if v is None:
            v = self.leaf(i)

        self.tree[v] = self.stat([self.tree[v], a])

        if v != 0:
            return self.update(i, a, v=self.parent(v))


class SegmentTreeSum(SegmentTree):

    def stat(self, iterable):
        return sum(iterable)

    def default(self):
        return 0

    def update(self, i, a, v=None):
        if v is None:
            v = self.leaf(i)
            self._diff = a - self.array[i]

        self.tree[v] += self._diff

        if v != 0:
            return self.update(i, a, v=self.parent(v))


if __name__ == '__main__':
    from doctest import testmod

    testmod()
