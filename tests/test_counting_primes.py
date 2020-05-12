from os.path import dirname
from pathlib import Path

import pytest
from .utils import collect_cases, _TestCaseMixin

from snippets import prime


def solve(i):
    """
    Examples
    --------
    >>> solve(10)
    4
    >>> solve(100)
    25
    """
    return len(prime(i))


class TestCase(_TestCaseMixin):

    directory = Path(dirname(__file__)) / 'library-checker-problems/math/counting_primes'
    pattern_in = 'in/small_*.in'
    pattern_out = 'out/small_*.out'

    cases = collect_cases(directory, pattern_in, pattern_out)
    solve = solve

    @classmethod
    def read_i(cls, f):
        return int(f.read())

    @classmethod
    def read_o(cls, f):
        return int(f.read())

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        self._test_for_case(*case)
