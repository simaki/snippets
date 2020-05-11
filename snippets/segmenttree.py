

class SegmentTree:
    """
    n_array = 4

    0-+-1-+-3
      |   +-4
      +-2-+-5
          +-6

    Attributes
    ----------
    - n_array : int
        Length of the array.
    - n_tree : int
        Length of the tree.
    - tree : list
        Segment tree.
    - section : list of (int, int)
        Section of each vertex.

    Examples
    --------
    >>> array = [5, 3, 7, 9, 1, 4, 6, 2]
    >>> st = SegmentTree(array)
    >>> st.tree
    [1, 3, 1, 3, 7, 1, 2, 5, 3, 7, 9, 1, 4, 6, 2]
    >>> st.min(0, 1)
    5
    >>> st.min(0, 7)
    1
    >>> st.update(0, 2).tree
    [1, 2, 1, 2, 7, 1, 2, 2, 3, 7, 9, 1, 4, 6, 2]
    """

    inf = float('inf')

    def __init__(self, array):
        self.array = array

        self.n_array = len(self.array)
        self.n_tree = 2 * self.n_array - 1
        self.tree = self._get_tree()
        self.section = self._get_section()

    def _get_tree(self):
        tree = [self.inf for _ in range(self.n_tree)]

        for i_tree in range(self.n_tree - 1, -1, -1):
            if i_tree >= self.n_array - 1:
                tree[i_tree] = self.array[i_tree - self.n_array + 1]
            else:
                c0, c1 = self.childs(i_tree)
                tree[i_tree] = min(tree[c0], tree[c1])

        return tree

    def _get_section(self):
        section = [None for _ in range(self.n_tree)]

        for i_tree in range(self.n_tree - 1, -1, -1):
            if i_tree >= self.n_array - 1:
                i = i_tree - self.n_array + 1
                section[i_tree] = (i, i + 1)
            else:
                c0, c1 = self.childs(i_tree)
                section[i_tree] = (section[c0][0], section[c1][1])

        return section

    def min(self, il, ir, v=0):
        """
        Return min(array[il:ir]).
        """
        sl, sr = self.section[v]
        if ir <= sl or ir <= sl:
            return self.inf
        elif il <= sl and sr <= ir:
            return self.tree[v]
        else:
            c0, c1 = self.childs(v)
            return min(self.min(il, ir, c0), self.min(il, ir, c1))

    def childs(self, v):
        return (2 * v + 1, 2 * v + 2)

    def parent(self, v):
        return (v - 1) // 2

    def update(self, i, a):
        v = i + self.n_array - 1
        while v != 0:
            self.tree[v] = min(self.tree[v], a)
            v = self.parent(v)

        return self



if __name__ == '__main__':
    from doctest import testmod

    testmod()
