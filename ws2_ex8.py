from search import *

class node():

    n = 0
    _2_n = None
    _2_n_1 = None

    def __init__(self, n):
        self.n = n

    def rec(self):
        if 2 * self.n <= 15:
            self._2_n = node(2 * self.n)
            self._2_n.rec()
        if 2 * self.n + 1 <= 15:
            self._2_n_1 = node(2 * self.n + 1)
            self._2_n_1.rec()

    def print_it(self):
        print(self.n)
        if self._2_n is not None:
            self._2_n.print_it()
        if self._2_n_1 is not None:
            self._2_n_1.print_it()

space = list()

first = node(1)
first.rec()

def print_this():
    first.print_it()

def ex8():
    arvore = Graph()
    passos = 7  # numero de nós
    for passo in range(passos):
        arvore.connect(passo + 1, 2 * (passo + 1))
        arvore.connect(passo + 1, 2 * (passo + 1) + 1)
    arvore.make_undirected()

    for passo in arvore.nodes():
        print(passo)

    problem = GraphProblem(1, 11, arvore)
    print(breadth_first_tree_search(problem).solution())
    print(breadth_first_tree_search(problem).path())


def ex():
    print("\n\n\n\n\n\n\n\n\n\n")
    passos = 15
    import math
    print(int(math.pow(2, 0)))
    print(int(math.pow(2, 1)))
    print(int(math.pow(2, 2)))
    print(int(math.pow(2, 3)))

"""
          1
    2            3
 4     5      6      7
8 9  10 11  12 13  14 15

...........1............
........../.\...........
........./...\..........
......../.....\.........
......./.......\........
....../.........\.......
....2............3......
.../.\........../..\....
../...\......../....\...
.4.....5......6......7..
/.\.../.\..../.\..../.\.
8.9..10.11..12.13..14.15

2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
"""