from os.path import dirname
from pathlib import Path

import pytest

from snippets import prime_factorization


def solve(i):
    """
    Examples
    --------
    >>> i = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> for line in solve(i):
    ...     print(line)
    [0]
    [1, 2]
    [1, 3]
    [2, 2, 2]
    [1, 5]
    [2, 2, 3]
    [1, 7]
    [3, 2, 2, 2]
    [2, 3, 3]
    [2, 2, 5]
    """
    q = i[0]

    o = []
    for n in i[1:]:
        dict_p = prime_factorization(n)
        n_p = sum([power for power in dict_p.values()])
        line = [n_p]
        for p, power in dict_p.items():
            line += [p] * power
        o.append(line)
    return o


def f_in_out():
    cases = Path(dirname(__file__)) / 'library-checker-problems/math/factorize/'
    f = []
    for f_in, f_out in zip(sorted(cases.glob('in/small_*.in')), sorted(cases.glob('out/small_*.out'))):
        f.append([f_in, f_out])
    return f


f = f_in_out()


class TestSolve:

    solve = solve

    @classmethod
    def _test_for_case(cls, f_in, f_out, f_a=None):
        with open(f_in) as f:
            i = [int(line) for line in f.readlines()]
        with open(f_out) as f:
            o_expected = [list(map(int, line.split())) for line in f.readlines()]

        assert cls.solve(i) == o_expected

    @pytest.mark.parametrize('f', f)
    def test(self, f):
        f_in, f_out = f
        self._test_for_case(f_in, f_out)

