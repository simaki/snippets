from os.path import dirname
from pathlib import Path

import pytest
from .utils import collect_cases, _TestCaseMixin

from snippets import z_algorithm


def solve(i):
    """
    Examples
    --------
    >>> i = 'abcbcba'
    >>> solve(i)
    [7, 0, 0, 0, 0, 0, 1]
    """
    return z_algorithm(i)


class TestCase(_TestCaseMixin):

    directory = Path(dirname(__file__)) / 'library-checker-problems/string/zalgorithm/'
    pattern_in = 'in/*.in'
    pattern_out = 'out/*.out'

    cases = collect_cases(directory, pattern_in, pattern_out)
    solve = solve

    @classmethod
    def read_i(cls, f):
        return f.read().strip()

    @classmethod
    def read_o(cls, f):
        return list(map(int, f.read().split()))

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        self._test_for_case(*case)
