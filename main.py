from backtracking import Backtracking
from graph import Graph
from insert import PopulateGraph

graph = Graph()
populateGraph = PopulateGraph(graph)
# graph.print_graph()

backtracking = Backtracking(graph)

print(backtracking.run())
graph.print_graph_with_colors()
print(graph.check_solution())