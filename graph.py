# -*- coding: utf-8 -*-
class Graph:
    def __init__(self):
        self.nodes = {}
        self.names = {}
        self.names[1] = "Acre"
        self.names[2] = "Alagoas"
        self.names[3] = "Amapá"
        self.names[4] = "Amazonas"
        self.names[5] = "Bahia"
        self.names[6] = "Ceará"
        self.names[7] = "Distrito Federal"
        self.names[8] = "Espírito Santo"
        self.names[9] = "Goiás"
        self.names[10] = "Maranhão"
        self.names[11] = "Mato Grosso"
        self.names[12] = "Mato Grosso do Sul"
        self.names[13] = "Minas Gerais"
        self.names[14] = "Pará"
        self.names[15] = "Paraíba"
        self.names[16] = "Paraná"
        self.names[17] = "Pernambuco"
        self.names[18] = "Piauí"
        self.names[19] = "Rio de Janeiro"
        self.names[20] = "Rio Grande do Norte"
        self.names[21] = "Rio Grande do Sul"
        self.names[22] = "Rondônia"
        self.names[23] = "Roraima"
        self.names[24] = "Santa Catarina"
        self.names[25] = "São Paulo"
        self.names[26] = "Sergipe"
        self.names[27] = "Tocantins"

    def get_adjacency(self, id):
        return self.nodes[id]['adjacency']

    def insert_node(self, node_id):
        self.nodes[node_id] = {'color': '', 'name': self.names[node_id], 'adjacency': []}

    def insert_adjacency(self, node_id, node_adjacent_id):
        self.nodes[node_id]['adjacency'].append(node_adjacent_id)

    def set_node_color(self, node_id, color):
        self.nodes[node_id]['color'] = color

    def set_node_name(self, node_id, name):
        self.nodes[node_id]['name'] = name

    def print_graph(self):
        for node_id in self.nodes:
            print(self.nodes[node_id]['name'])
            for adjacent_id in self.nodes[node_id]['adjacency']:
                print('\t '+str(self.names[adjacent_id]))
            print('\n')



