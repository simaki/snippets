from os.path import dirname
from pathlib import Path

import pytest
from .utils import collect_cases, _TestCaseMixin

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
    o = []
    for n in i[1:]:
        dict_p = prime_factorization(n)
        line = [sum(dict_p.values())]
        for p, power in dict_p.items():
            line += [p] * power
        o.append(line)
    return o


class TestCase(_TestCaseMixin):

    directory =  Path(dirname(__file__)) / 'library-checker-problems/math/factorize/'
    pattern_in = 'in/small_*.in'
    pattern_out = 'out/small_*.out'

    cases = collect_cases(directory, pattern_in, pattern_out)
    solve = solve

    @classmethod
    def read_i(cls, f):
        return [int(line) for line in f.readlines()]

    @classmethod
    def read_o(cls, f):
        return [list(map(int, line.split())) for line in f.readlines()]

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        self._test_for_case(*case)
