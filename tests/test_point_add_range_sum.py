from os.path import dirname
from pathlib import Path

import pytest

from snippets import SegmentTreeSum
from .utils import collect_cases, _TestCaseMixin


def solve(i):
    """
    Examples
    --------
    >>> i = [
    ...     [5, 5],
    ...     [1, 2, 3, 4, 5],
    ...     [1, 0, 5],
    ...     [1, 2, 4],
    ...     [0, 3, 10],
    ...     [1, 0, 5],
    ...     [1, 0, 3]
    ... ]
    >>> solve(i)
    [15, 7, 25, 6]
    """
    st = SegmentTreeSum(i[1])

    o = []
    for t, l, r in i[2:]:
        if t == 0:
            st.update(l, st.array[l] + r)
        else:
            o.append(st(l, r))
    return o


class TestCase(_TestCaseMixin):

    directory = Path(dirname(__file__)) / 'library-checker-problems/datastructure/point_add_range_sum/'
    pattern_in = 'in/small_*.in'
    pattern_out = 'out/small_*.out'

    cases = collect_cases(directory, pattern_in, pattern_out)
    solve = solve

    @classmethod
    def read_i(cls, f):
        return [list(map(int, line.split())) for line in f.readlines()]

    @classmethod
    def read_o(cls, f):
        return list(map(int, f.read().split()))

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        self._test_for_case(*case)
