from os.path import dirname
from pathlib import Path

import pytest

from snippets import UnionFind
from .utils import collect_cases, TestCaseMixin



def solve(i):
    """
    Examples
    --------
    >>> i = [
    ...     [4, 7],
    ...     [1 0 1],
    ...     [0 0 1],
    ...     [0 2 3],
    ...     [1 0 1],
    ...     [1 1 2],
    ...     [0 0 2],
    ...     [1 1 3],
    ... ]
    >>> solve(i)
    [0, 1, 0, 1]
    """
    n, q = i[0]

    uf = UnionFind(n)

    o = []
    for t, u, v in i[1:]:
        if t == 0:
            uf.union(u, v)
        else:
            connected = int(uf.find(u) == uf.find(v))
            o.append(connected)
    return o


class TestCase(TestCaseMixin):

    directory = Path(dirname(__file__)) / 'library-checker-problems/datastructure/unionfind'
    pattern_in = 'in/*.in'
    pattern_out = 'out/*.out'

    cases = collect_cases(directory, pattern_in, pattern_out)
    solver = solve

    @classmethod
    def read_i(cls, f):
        return [list(map(int, line.split())) for line in f.readlines()]

    @classmethod
    def read_o(cls, f):
        return [int(line) for line in f.readlines()]
