from os.path import dirname
from pathlib import Path

import pytest
from .utils import collect_cases, _TestCaseMixin


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


class TestCase(_TestCaseMixin):

    directory = Path(dirname(__file__)) / 'library-checker-problems/sample/aplusb/'
    pattern_in = 'in/*.in'
    pattern_out = 'out/*.out'

    cases = collect_cases(directory, pattern_in, pattern_out)
    solve = solve

    @classmethod
    def read_i(cls, f):
        return [int(i) for i in f.read().split()]

    @classmethod
    def read_o(cls, f):
        return int(f.read())

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        self._test_for_case(*case)
