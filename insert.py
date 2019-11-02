# coding=utf-8
class GraphPopulator:
    def __init__(self, graph):
        self.graph = graph

    def insert(self):
        for i in range(1, 28):
            self.graph.insert_node(i)

        self.graph.insert_adjacency(1, 4)
        self.graph.insert_adjacency(1, 22)

        self.graph.insert_adjacency(2, 17)
        self.graph.insert_adjacency(2, 26)
        self.graph.insert_adjacency(2, 5)

        self.graph.insert_adjacency(3, 14)

        self.graph.insert_adjacency(4, 23)
        self.graph.insert_adjacency(4, 14)
        self.graph.insert_adjacency(4, 22)
        self.graph.insert_adjacency(4, 1)
        self.graph.insert_adjacency(4, 11)

        self.graph.insert_adjacency(5, 27)
        self.graph.insert_adjacency(5, 18)
        self.graph.insert_adjacency(5, 17)
        self.graph.insert_adjacency(5, 2)
        self.graph.insert_adjacency(5, 26)
        self.graph.insert_adjacency(5, 8)
        self.graph.insert_adjacency(5, 13)
        self.graph.insert_adjacency(5, 9)

        self.graph.insert_adjacency(6, 17)
        self.graph.insert_adjacency(6, 18)
        self.graph.insert_adjacency(6, 15)
        self.graph.insert_adjacency(6, 20)

        self.graph.insert_adjacency(7, 9)
        self.graph.insert_adjacency(7, 13)

        self.graph.insert_adjacency(8, 13)
        self.graph.insert_adjacency(8, 19)
        self.graph.insert_adjacency(8, 5)

        self.graph.insert_adjacency(9, 7)
        self.graph.insert_adjacency(9, 13)
        self.graph.insert_adjacency(9, 11)
        self.graph.insert_adjacency(9, 12)
        self.graph.insert_adjacency(9, 27)
        self.graph.insert_adjacency(9, 5)

        self.graph.insert_adjacency(10, 14)
        self.graph.insert_adjacency(10, 27)
        self.graph.insert_adjacency(10, 18)

        self.graph.insert_adjacency(11, 4)
        self.graph.insert_adjacency(11, 14)
        self.graph.insert_adjacency(11, 27)
        self.graph.insert_adjacency(11, 9)
        self.graph.insert_adjacency(11, 12)
        self.graph.insert_adjacency(11, 22)

        self.graph.insert_adjacency(12, 9)
        self.graph.insert_adjacency(12, 11)
        self.graph.insert_adjacency(12, 25)
        self.graph.insert_adjacency(12, 16)
        self.graph.insert_adjacency(12, 13)

        self.graph.insert_adjacency(13, 5)
        self.graph.insert_adjacency(13, 19)
        self.graph.insert_adjacency(13, 8)
        self.graph.insert_adjacency(13, 25)
        self.graph.insert_adjacency(13, 9)
        self.graph.insert_adjacency(13, 12)
        self.graph.insert_adjacency(13, 7)

        self.graph.insert_adjacency(14, 11)
        self.graph.insert_adjacency(14, 27)
        self.graph.insert_adjacency(14, 10)
        self.graph.insert_adjacency(14, 4)
        self.graph.insert_adjacency(14, 23)
        self.graph.insert_adjacency(14, 3)

        self.graph.insert_adjacency(15, 6)
        self.graph.insert_adjacency(15, 17)
        self.graph.insert_adjacency(15, 20)
        self.graph.insert_adjacency(15, 20)

        self.graph.insert_adjacency(16, 25)
        self.graph.insert_adjacency(16, 12)
        self.graph.insert_adjacency(16, 24)

        self.graph.insert_adjacency(17, 2)
        self.graph.insert_adjacency(17, 5)
        self.graph.insert_adjacency(17, 18)
        self.graph.insert_adjacency(17, 6)
        self.graph.insert_adjacency(17, 15)

        self.graph.insert_adjacency(18, 10)
        self.graph.insert_adjacency(18, 27)
        self.graph.insert_adjacency(18, 6)
        self.graph.insert_adjacency(18, 17)
        self.graph.insert_adjacency(18, 5)

        self.graph.insert_adjacency(19, 25)
        self.graph.insert_adjacency(19, 8)
        self.graph.insert_adjacency(19, 13)

        self.graph.insert_adjacency(20, 6)
        self.graph.insert_adjacency(20, 15)

        self.graph.insert_adjacency(21, 24)

        self.graph.insert_adjacency(22, 1)
        self.graph.insert_adjacency(22, 4)
        self.graph.insert_adjacency(22, 11)
        #
        self.graph.insert_adjacency(23, 4)
        self.graph.insert_adjacency(23, 14)

        self.graph.insert_adjacency(24, 16)
        self.graph.insert_adjacency(24, 21)

        self.graph.insert_adjacency(25, 19)
        self.graph.insert_adjacency(25, 13)
        self.graph.insert_adjacency(25, 16)
        self.graph.insert_adjacency(25, 12)

        self.graph.insert_adjacency(26, 2)
        self.graph.insert_adjacency(26, 5)

        self.graph.insert_adjacency(27, 9)
        self.graph.insert_adjacency(27, 5)
        self.graph.insert_adjacency(27, 18)
        self.graph.insert_adjacency(27, 10)
        self.graph.insert_adjacency(27, 11)
        self.graph.insert_adjacency(27, 14)


    def insert_north(self):
        for i in range(1, 8):
            self.graph.insert_node(i)


        #1: "Acre", 2: "Amapá", 3: "Amazonas", 4: "Pará", 5: "Rondônia", 6: "Roraima", 7: "Tocantins"
        self.graph.insert_adjacency(1, 3)
        self.graph.insert_adjacency(1, 5)

        self.graph.insert_adjacency(2, 4)

        self.graph.insert_adjacency(3, 1)
        self.graph.insert_adjacency(3, 4)
        self.graph.insert_adjacency(3, 5)
        self.graph.insert_adjacency(3, 6)

        self.graph.insert_adjacency(4, 2)
        self.graph.insert_adjacency(4, 3)
        self.graph.insert_adjacency(4, 6)
        self.graph.insert_adjacency(4, 7)

        self.graph.insert_adjacency(5, 1)
        self.graph.insert_adjacency(5, 3)

        self.graph.insert_adjacency(6, 3)
        self.graph.insert_adjacency(6, 4)

        self.graph.insert_adjacency(7, 4)
