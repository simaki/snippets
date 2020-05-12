from os.path import dirname
from pathlib import Path

import pytest


def solve(i):
    """
    Examples
    --------
    >>> i = [1234, 5678]
    >>> solve(i)
    6912
    """
    a, b = i
    return a + b


def collect_cases():
    directory = Path(dirname(__file__)) / 'library-checker-problems/sample/aplusb/'
    glob_i = sorted(directory.glob('in/*.in'))
    glob_o = sorted(directory.glob('out/*.out'))
    return list(zip(glob_i, glob_o))


class TestCase:

    solve = solve
    cases = collect_cases()

    @classmethod
    def _assert_case(cls, f_i, f_o):
        with open(f_i) as f:
            i = [int(j) for j in f.read().split()]
        with open(f_o) as f:
            o_expected = int(f.read().strip('\n'))

        assert cls.solve(i) == o_expected

    @pytest.mark.parametrize('case', cases)
    def test_case(self, case):
        f_i, f_o = case
        self._assert_case(f_i, f_o)
