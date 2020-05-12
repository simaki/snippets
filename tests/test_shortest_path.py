from os.path import dirname
from pathlib import Path

import pytest
from .utils import collect_cases, _TestCaseMixin

from snippets import Graph, dijkstra


def solve(i):
    """
    Examples
    --------
    >>> i = [
    ...     [5, 7, 2, 3],
    ...     [0, 3, 5],
    ...     [0, 4, 3],
    ...     [2, 4, 2],
    ...     [4, 3, 10],
    ...     [4, 0, 7],
    ...     [2, 1, 5],
    ...     [1, 0, 1],
    ... ]
    >>> solve(i)
    [[11, 3], [2, 1], [1, 0], [0, 3]]
    """
    s, t = i[0][2], i[0][3]
    e = [(line[0], line[1]) for line in i[1:]]
    we = [line[2] for line in i[1:]]

    graph = Graph(i[0][0], e, we=we)

    d, prev = dijkstra(graph, s)
    dt = d[t]

    if dt == float('inf'):
        return [[-1]]
    else:
        path = [t]
        while prev[t] is not None:
            t = prev[t]
            path.append(t)

        return [[dt, len(path) - 1]] + [[p0, p1] for p0, p1 in zip(path[::-1], path[:-1][::-1])]



class TestCase(_TestCaseMixin):

    directory = Path(dirname(__file__)) / 'library-checker-problems/graph/shortest_path'
    pattern_in = 'in/small_*.in'
    pattern_out = 'out/small_*.out'

    cases = collect_cases(directory, pattern_in, pattern_out)
    solve = solve

    @classmethod
    def read_i(cls, f):
        return [list(map(int, line.split())) for line in f.readlines()]

    @classmethod
    def read_o(cls, f):
        return [list(map(int, line.split())) for line in f.readlines()]

    @pytest.mark.parametrize('case', cases)
    def test(self, case):
        self._test_for_case(*case)
