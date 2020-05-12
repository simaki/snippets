from os.path import dirname
from pathlib import Path

import pytest

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


def collect_cases():
    directory = Path(dirname(__file__)) / 'library-checker-problems/math/enumerate_primes'
    glob_i = sorted(directory.glob('in/example_*.in'))
    glob_o = sorted(directory.glob('out/example_*.out'))
    return list(zip(glob_i, glob_o))



class TestSolve:

    solve = solve
    cases = collect_cases()

    @classmethod
    def _assert_case(cls, f_i, f_o):
        with open(f_i) as f:
            i = [int(line) for line in f.read().split()]
        with open(f_o) as f:
            o_expected = [list(map(int, line.split())) for line in f.readlines()]

        assert cls.solve(i) == o_expected

    @pytest.mark.parametrize('case', cases)
    def test_case(self, case):
        f_i, f_o = case
        self._assert_case(f_i, f_o)
