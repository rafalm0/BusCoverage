class Node:  # clase nao usada

    def __init__(self, node_id):
        self.id = node_id
        self.edge_list = []
        return

    def add_edge(self, edge):
        self.edge_list.append(edge)
        return


class NodeDualSided:

    def __init__(self, node_id, long, lat):
        self.street_lat = float('inf')  # latitude referente ao mapa do openstreetmap
        self.street_long = float('inf')  # longitude referente ao mapa do openstreetmap
        self.street_name = ''
        self.long = long  # longitude no grafo de parada de onibus
        self.lat = lat  # latitude no grafo de parada de onibus
        self.id = node_id
        self.edge_out = []  # ruas que saem do node
        self.edge_in = []  # ruas que entram no node
        return

    def add_edge(self, edge_dual_sided):  # processo de adicionar referencia ao edge no node
        if self == edge_dual_sided.source:
            self.edge_out.append(edge_dual_sided)
        else:
            self.edge_in.append(edge_dual_sided)
        return
