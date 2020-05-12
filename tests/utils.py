from abc import ABCMeta, abstractmethod
from os.path import dirname
from pathlib import Path

import pytest


def collect_cases(directory, pattern_in, pattern_out):
    glob_i = sorted(directory.glob(pattern_in))
    glob_o = sorted(directory.glob(pattern_out))
    return list(zip(glob_i, glob_o))


class TestCaseMixin(metaclass=ABCMeta):

    cases = collect_cases(
        Path(dirname(__file__)) / 'library-checker-problems/datastructure/unionfind',
        'in/*.in',
        'out/*.out',
    )

    solver = lambda x: None

    @classmethod
    def solve(cls, i):
        return cls.solver(i)

    @classmethod
    def read_i(cls, f):
        """
        Read input from a file.
        """

    @classmethod
    def read_o(cls, f):
        """
        Read output from a file.
        """

    @classmethod
    def _test_for_case(cls, f_in, f_out, f_a=None):
        with open(f_in) as f:
            i = cls.read_i(f)
        with open(f_out) as f:
            o_expected = cls.read_o(f)

        assert cls.solve(i) == o_expected

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        # f_in, f_out = case
        self._test_for_case(*case)

