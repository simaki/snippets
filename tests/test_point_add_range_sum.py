from os.path import dirname
from pathlib import Path

import pytest

from snippets import SegmentTreeSum


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
            st.update(l, r)
        else:
            o.append(st(l, r))
    return o


def collect_cases():
    directory = Path(dirname(__file__)) / 'library-checker-problems/datastructure/point_add_range_sum'
    glob_i = sorted(directory.glob('in/small_*.in'))
    glob_o = sorted(directory.glob('out/small_*.out'))
    return list(zip(glob_i, glob_o))


class TestSolve:

    solve = solve
    cases = collect_cases()

    @classmethod
    def _assert_case(cls, f_i, f_o):
        with open(f_i) as f:
            i = int(f.read())
        with open(f_o) as f:
            o_expected = int(f.read())

        assert cls.solve(i) == o_expected

    @pytest.mark.parametrize('case', cases)
    def test_case(self, case):
        f_i, f_o = case
        self._assert_case(f_i, f_o)


class TestCase:

    solve = solve
    cases = collect_cases()

    def read_i(f):
        return [list(map(int, line.split())) for line in f.readlines()]

    def read_o(f):
        return [int(line) for line in f.readlines()]

    @classmethod
    def _test_for_case(cls, f_in, f_out, f_a=None):
        with open(f_in) as f:
            i = [list(map(int, line.split())) for line in f.readlines()]
        with open(f_out) as f:
            o_expected = [int(line) for line in f.readlines()]

        assert cls.solve(i) == o_expected

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        f_in, f_out = case
        self._test_for_case(f_in, f_out)

