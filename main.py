from backtracking import Backtracking
from breadth import Breadth
from graph import Graph
from insert import GraphPopulator
import time

if __name__ == '__main__':

    # graph = Graph('all')
    # populator = GraphPopulator(graph)
    # populator.insert()
    # backtracking = Backtracking(graph)
    # backtracking.run()

    graph = Graph('north')
    populator = GraphPopulator(graph)
    populator.insert_north()
    breadth = Breadth(graph)
    breadth.breadth()

# graph.print_graph_with_colors()


