from os.path import dirname
from pathlib import Path

import pytest
from .utils import collect_cases, _TestCaseMixin

from snippets import prime


def solve(i):
    """
    Examples
    --------
    >>> i = [100, 3, 1]
    >>> solve(i)
    [[25, 8], [3, 11, 19, 31, 43, 59, 71, 83]]
    """
    n, a, b = i

    p = prime(n)
    pi = len(p)
    x = (pi - b) // a
    return [[pi, x], p[b::a]]


class TestCase(_TestCaseMixin):

    directory = Path(dirname(__file__)) / 'library-checker-problems/math/enumerate_primes'
    pattern_in = 'in/example_*.in'
    pattern_out = 'out/example_*.out'

    cases = collect_cases(directory, pattern_in, pattern_out)
    solve = solve

    @classmethod
    def read_i(cls, f):
        return [int(line) for line in f.read().split()]

    @classmethod
    def read_o(cls, f):
        return [list(map(int, line.split())) for line in f.readlines()]

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        self._test_for_case(*case)
