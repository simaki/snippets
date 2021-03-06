from abc import ABCMeta, abstractmethod
from os.path import dirname
from pathlib import Path

import pytest


def collect_cases(directory, pattern_in, pattern_out):
    glob_i = sorted(directory.glob(pattern_in))
    glob_o = sorted(directory.glob(pattern_out))
    return list(zip(glob_i, glob_o))


def not_implemented(*arg):
    raise NotImplementedError('Solver is not implemented')


class _TestCaseMixin(metaclass=ABCMeta):

    cases = []
    solve = not_implemented

    @classmethod
    def solver(cls, i):
        return cls.solve(i)

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
    def _test_for_case(cls, f_i, f_o):
        with open(f_i) as f:
            i = cls.read_i(f)
        with open(f_o) as f:
            o_exp = cls.read_o(f)
        o = cls.solver(i)
        print(o)
        print(o_exp)
        assert o == o_exp

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        self._test_for_case(*case)

