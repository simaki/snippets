from os.path import dirname
from pathlib import Path

import pytest

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


def collect_cases():
    directory = Path(dirname(__file__)) / 'library-checker-problems/math/counting_primes'
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

