from search import *

arvore = Graph()
passos = 7


def ex8_1():
    for passo in range(passos):
        arvore.connect(passo + 1, 2 * (passo + 1))
        arvore.connect(passo + 1, 2 * (passo + 1) + 1)

    print('\n\nGraph:')
    for passo in arvore.nodes():
        print(passo)


def ex8_2_bfs(problem):
    print('\n\nBFS:')
    bfs = breadth_first_tree_search(problem)
    print('Solution: ', bfs.solution())
    print('Path: ', bfs.path())


def ex8_2_dfs(problem):
    limit = 3
    print('\n\nDFS with limit {}:'.format(limit))
    cutoff = 'cutoff'
    dls = depth_limited_search(problem, limit)
    if dls != cutoff:
        print('Solution: ', depth_first_tree_search(problem).solution())
    else:
        print('Solution: ', dls)


def ex8_2_ids(problem):
    print('\n\nIDS:')
    print('Solution: ', iterative_deepening_search(problem))


def ex8_2():
    problem = GraphProblem(1, 11, arvore)
    ex8_2_bfs(problem)
    ex8_2_dfs(problem)
    ex8_2_ids(problem)


def main():
    ex8_1()
    ex8_2()

