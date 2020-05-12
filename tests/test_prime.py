from os.path import dirname
from pathlib import Path

import pytest

# from snippets import prime


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


@pytest.fixture
def f_in_out():
    cases = Path(dirname(__file__)) / 'library-checker-problems/math/counting_primes/'
    f = []
    for f_in, f_out in zip(sorted(cases.glob('in/small_*.in')), sorted(cases.glob('out/small_*.out'))):
        f.append([f_in, f_out])
    return f



class TestSolve:

    solve = solve

    @classmethod
    def _test_for_case(cls, f_in, f_out, f_a=None):
        with open(f_in) as f:
            i = int(f.read())
        with open(f_out) as f:
            o_expected = int(f.read())

        assert cls.solve(i) == o_expected

    @pytest.mark.parametrize('f_in_out', f_in_out)
    def test(self, f_in_out):
        f_in, f_out = f_in_out
        self._test_for_case(f_in, f_out)

