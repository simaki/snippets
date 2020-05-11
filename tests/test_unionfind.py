from os.path import dirname
from pathlib import Path

import pytest

from snippets import UnionFind


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


def f_in_out():
    cases = Path(dirname(__file__)) / 'library-checker-problems/datastructure/unionfind/'
    f = []
    for f_in, f_out in zip(sorted(cases.glob('in/*.in')), sorted(cases.glob('out/*.out'))):
        f.append([f_in, f_out])
    return f


f = f_in_out()


class TestSolve:

    solve = solve

    @classmethod
    def _test_for_case(cls, f_in, f_out, f_a=None):
        with open(f_in) as f:
            i = [list(map(int, line.split())) for line in f.readlines()]
        with open(f_out) as f:
            o_expected = [int(line) for line in f.readlines()]

        assert cls.solve(i) == o_expected

    @pytest.mark.parametrize('f', f)
    def test(self, f):
        f_in, f_out = f
        self._test_for_case(f_in, f_out)

