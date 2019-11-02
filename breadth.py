import Queue
from graph import Graph

class Breadth:


    def __init__(self, graph):
        self.graph = graph
        self.number_of_states = len(graph.get_all_nodes())
        self.open = Queue.Queue()
        self.all_nodes = []

    def breadth(self):
        first_node = \
            {
                "id": 0,
                "state_id": 7,
                "color": '',
                "parent_id": None,
                "neighbors": self.graph.get_adjacency(7),
                "path": [0]
            }
        self.all_nodes.append(first_node)
        self.open.put(first_node)

        i = 1
        path = []
        while not self.open.empty():

            state = self.open.get()

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
                self.open.put(node)
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
                "path": path
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