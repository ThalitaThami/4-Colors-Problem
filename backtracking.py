class Backtracking:
    def __init__(self, graph):
        self.graph = graph
        self.path = []

    def get_path(self):
        return self.path

    def run(self):
        path = []
        self.backtracking(1, path)

    def backtracking(self, node_id, path):
        self.path = path

        if node_id in path:
            return

        if not self.graph.can_color(node_id):
            return

        path.append(node_id)
        cor = self.graph.smaller_color(node_id)
        self.graph.set_node_color(node_id, cor)

        print(str(self.graph.names[node_id])+" => "+str(self.graph.get_node_color(node_id)))

        for adjacent_id in self.graph.get_adjacency(node_id):
            self.backtracking(adjacent_id, path)