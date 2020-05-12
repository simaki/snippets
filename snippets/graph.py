from heapq import heapify, heappush, heappop


class Graph:
    """
    Examples
    --------
    >>> n = 5
    >>> e = [
    ...     [0, 3],
    ...     [0, 4],
    ...     [2, 4],
    ...     [4, 3],
    ...     [4, 0],
    ...     [2, 1],
    ...     [1, 0],
    ... ]
    >>> wv = [1, 2, 3, 4, 5]
    >>> we = [5, 3, 2, 10, 7, 5, 1]
    >>> graph = Graph(n, e, we=we)
    """
    def __init__(self, n, e, wv=None, we=None):
        self.n = n
        self.e = list(map(tuple, e))
        self.wv = wv
        self.we = we

        self.adjlist = self.__get_adjlist()
        self.wedict = self.__get_wedict()

    def __get_adjlist(self):
        adjlist = [[] for _ in range(self.n)]

        for v0, v1 in self.e:
            adjlist[v0].append(v1)

        return adjlist

    def __get_wedict(self):
        return dict(zip(self.e, self.we))


def dijkstra(graph, s):
    """
    Examples
    --------
    >>> n = 5
    >>> e = [
    ...     (0, 3),
    ...     (0, 4),
    ...     (2, 4),
    ...     (4, 3),
    ...     (4, 0),
    ...     (2, 1),
    ...     (1, 0),
    ... ]
    >>> wv = [1, 2, 3, 4, 5]
    >>> we = [5, 3, 2, 10, 7, 5, 1]
    >>> graph = Graph(n, e, we=we)
    >>> dijkstra(graph, 2)[0][3]
    11
    """
    INF = float('inf')

    d = [INF for _ in range(graph.n)]
    d[s] = 0
    prev = [None for _ in range(graph.n)]

    queue = []
    heappush(queue, (0, s))

    while queue:
        di, v = heappop(queue)
        for neighbor in graph.adjlist[v]:
            dtmp = d[v] + graph.wedict[(v, neighbor)]
            if dtmp < d[neighbor]:
                d[neighbor] = dtmp
                prev[neighbor] = v
                heappush(queue, (dtmp, neighbor))

    return d, prev


if __name__ == '__main__':
    from doctest import testmod

    testmod()
