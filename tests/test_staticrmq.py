from os.path import dirname
from pathlib import Path

import pytest

from snippets import SegmentTreeMin
from .utils import collect_cases, _TestCaseMixin


directory = Path(dirname(__file__)) / 'library-checker-problems/datastructure/staticrmq/'
pattern_in = 'in/small_*.in'
pattern_out = 'out/small_*.out'


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


class TestCase(_TestCaseMixin):

    cases = collect_cases(directory, pattern_in, pattern_out)
    solve = solve

    @classmethod
    def read_i(cls, f):
        return [list(map(int, line.split())) for line in f.readlines()]

    @classmethod
    def read_o(cls, f):
        return [int(line) for line in f.readlines()]

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        self._test_for_case(*case)
