import Queue
from graph import Graph

class Greedy:


    def __init__(self, graph):
        self.graph = graph
        self.number_of_states = len(graph.get_all_nodes())
        self.open = []
        self.all_nodes = []

    def sort_open_list(self):
        self.open.sort(key=lambda x: x['heuristics'], reverse=True)

    def greedy(self):
        first_node = \
            {
                "id": 0,
                "state_id": 4,
                "color": '',
                "parent_id": None,
                "neighbors": self.graph.get_adjacency(4),
                "path": [0],
                "heuristics": self.graph.get_node_heuristics(4)
            }

        self.all_nodes.append(first_node)
        self.open.append(first_node)

        i = 1
        path = []

        while len(self.open) > 0:

            self.sort_open_list()

            state = self.open.pop()

            color = self.smallest_color_on_path(state)

            if color == 5:
                continue

            state['color'] = color

            if len(state['path']) == 7:
                print i
                return self.printa(state['path'])


            for each_state in range(1, self.number_of_states + 1):

                if self.is_in_path(state['path'], each_state, i):
                    continue

                node = self.create_node(i, each_state, state['id'],state['path'][:])
                self.open.append(node)
                i += 1

            path = state['path']

        return self.printa(path)



    def create_node(self, id, state_id, parent_id, path):
        node = \
            {
                "id": id,
                "state_id":state_id,
                "color": '',
                "parent_id": parent_id,
                "neighbors": self.graph.get_adjacency(state_id),
                "path": path,
                "heuristics": self.graph.get_node_heuristics(state_id)
            }

        node['path'].append(node['id'])
        self.all_nodes.append(node)
        return node

    def smallest_color_on_path(self, node):
        if len(node['path']) == 1:
            return  1

        colors = {1, 2, 3, 4}
        for color in colors:
            can_color = True
            for id_node in node['path']:
                node_in_path = self.get_node_by_id(id_node)
                if self.is_adjacent(node['state_id'], node_in_path['state_id']):
                    if node_in_path['color'] == color:
                        can_color = False

            if can_color:
                return color

        return 5

    def get_node_by_id(self, node_id):
        for node in self.all_nodes:
            if node['id'] == node_id:
                return node

        return None

    def is_adjacent(self, state_id, adjacent_state_id):
        if adjacent_state_id in self.graph.get_adjacency(state_id):
            return  True
        return False

    def is_in_path(self, path, state_id, id):
        if len(path) == 1:
            return False

        for node_id in path:
            if node_id == id:
                continue

            if self.all_nodes[node_id]['state_id'] == state_id:
                return True
        return False


    def printa(self, path):
        for index in path:
            node = self.get_node_by_id(index)
            print str(node['state_id']) + '=>' + str(node['color'])