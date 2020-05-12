"""
Segment Tree
"""
from os.path import dirname
from pathlib import Path

import pytest

from snippets import SegmentTreeMin


def solve(i):
    """
    Examples
    --------
    >>> i = [
    ...     [4, 10],
    ...     [2, 10, 1, 100],
    ...     [0, 1],
    ...     [0, 2],
    ...     [0, 3],
    ...     [0, 4],
    ...     [1, 2],
    ...     [1, 3],
    ...     [1, 4],
    ...     [2, 3],
    ...     [2, 4],
    ...     [3, 4],
    ... ]
    >>> solve(i)
    [2, 2, 1, 1, 10, 1, 1, 1, 1, 100]
    """
    n, q = i[0]
    a = i[1]
    st = SegmentTreeMin(a)
    return [st(il, ir) for il, ir in i[2:]]


def f_in_out():
    cases = Path(dirname(__file__)) / 'library-checker-problems/datastructure/staticrmq/'
    f = []
    for f_in, f_out in zip(sorted(cases.glob('in/small_*.in')), sorted(cases.glob('out/small_*.out'))):
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

