# -*- coding: utf-8 -*-
class Graph:
    def __init__(self, region):
        self.nodes = {}
        self.colors = {1, 2, 3, 4}

        if region == "all":
            self.names = {1: "Acre", 2: "Alagoas", 3: "Amapá", 4: "Amazonas", 5: "Bahia", 6: "Ceará", 7: "Distrito Federal",
                      8: "Espírito Santo", 9: "Goiás", 10: "Maranhão", 11: "Mato Grosso", 12: "Mato Grosso do Sul",
                      13: "Minas Gerais", 14: "Pará", 15: "Paraíba", 16: "Paraná", 17: "Pernambuco", 18: "Piauí",
                      19: "Rio de Janeiro", 20: "Rio Grande do Norte", 21: "Rio Grande do Sul", 22: "Rondônia",
                      23: "Roraima", 24: "Santa Catarina", 25: "São Paulo", 26: "Sergipe", 27: "Tocantins"}

        if region == "north":
            self.names = {1: "Acre", 2: "Amapá", 3: "Amazonas", 4: "Pará", 5: "Rondônia", 6: "Roraima", 7: "Tocantins"}


    def get_adjacency(self, node_id):
        return self.nodes[node_id]['adjacency']

    def insert_node(self, node_id):
        self.nodes[node_id] = {'color': '', 'name': self.names[node_id], 'adjacency': []}

    def insert_adjacency(self, node_id, adjacent_id):
        self.nodes[node_id]['adjacency'].append(adjacent_id)

    def set_node_color(self, node_id, color):
        self.nodes[node_id]['color'] = color

    def get_node_color(self, node_id):
        return self.nodes[node_id]['color']

    def set_node_name(self, node_id, name):
        self.nodes[node_id]['name'] = name

    def get_all_nodes(self):
        return self.nodes

    def print_graph(self):
        for node_id in self.nodes:
            print(self.nodes[node_id]['name'])
            for adjacent_id in self.nodes[node_id]['adjacency']:
                print('\t ' + str(self.names[adjacent_id]))
            print('\n')

    def print_graph_with_colors(self):
        for node_id in self.nodes:
            print(self.nodes[node_id]['name'])
            print(self.nodes[node_id]['color'])

            for adjacent_id in self.nodes[node_id]['adjacency']:
                print('\t ' + str(self.names[adjacent_id]) + ": " + str(self.get_node_color(adjacent_id)))

            print('\n')

    def smaller_color(self, node_id):
        for color in self.colors:
            can_color = True

            for adjacent_id in self.nodes[node_id]['adjacency']:
                if self.nodes[adjacent_id]['color'] == color:
                    can_color = False

            if can_color:
                return color

        return 5

    def can_color(self, adjacent_id):
        return self.smaller_color(adjacent_id) < 5

    def check_solution(self):
        for node_id in self.nodes:
            node_color = self.nodes[node_id]['color']
            for adjacent_id in self.get_adjacency(node_id):
                if self.nodes[adjacent_id]['color'] == node_color:
                    print(self.names[node_id])
                    print(self.names[adjacent_id])
                    return False

        return True
