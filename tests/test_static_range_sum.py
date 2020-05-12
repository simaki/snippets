from os.path import dirname
from pathlib import Path

import pytest

from snippets import RangeSum


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


def collect_cases():
    directory = Path(dirname(__file__)) / 'library-checker-problems/datastructure/static_range_sum/'
    glob_i = sorted(directory.glob('in/*.in'))
    glob_o = sorted(directory.glob('out/*.out'))
    return list(zip(glob_i, glob_o))



class TestSolve:

    solve = solve
    cases = collect_cases()

    @classmethod
    def _assert_case(cls, f_i, f_o):
        with open(f_i) as f:
            i = [list(map(int, line.split())) for line in f.readlines()]
        with open(f_o) as f:
            o_expected = [int(line) for line in f.readlines()]

        assert cls.solve(i) == o_expected

    @pytest.mark.parametrize('case', cases)
    def test_case(self, case):
        f_i, f_o = case
        self._assert_case(f_i, f_o)
