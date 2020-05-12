from os.path import dirname
from pathlib import Path

import pytest

from snippets import RangeSum
from .utils import collect_cases, _TestCaseMixin


directory = Path(dirname(__file__)) / 'library-checker-problems/datastructure/static_range_sum/'
pattern_in = 'in/example_*.in'
pattern_out = 'out/example_*.out'


def solve(i):
    """
    Examples
    --------
    >>> i = [
    ...     [5, 5],
    ...     [1, 10, 100, 1000, 10000],
    ...     [2, 3],
    ...     [0, 3],
    ...     [2, 5],
    ...     [3, 4],
    ...     [0, 5],
    ...     ]
    >>> solve(i)
    [100, 111, 11100, 1000, 11111]
    """
    n, q = i[0]
    a = i[1]
    rs = RangeSum(a)

    return [rs(il, ir) for il, ir in i[2:]]


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
