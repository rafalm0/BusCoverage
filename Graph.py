from Node import Node
from Node import NodeDualSided
from Edge import Edge
from Edge import EdgeDualSided
from Route import Route
import matplotlib.pyplot as plt


class Graph:  # classe nao sendo usada atualmente

    def __init__(self):
        self.next_id = 0
        self.nodes = {}
        self.edges = {}
        self.total_distance = 0.0
        self.routes = {}
        return

    def add_node(self, node_id):
        new_node = Node(node_id)
        self.nodes[node_id] = new_node
        return

    def add_edge(self, edge_distance, nodes):
        both_nodes = [self.nodes[nodes[0]], self.nodes[nodes[1]]]
        edge = Edge(both_nodes, float(edge_distance), self.next_id)
        for node in nodes:
            self.nodes[node].add_edge(edge)
        self.edges[self.next_id] = edge
        self.total_distance = self.total_distance + float(edge_distance)
        self.next_id = self.next_id + 1
        return edge

    def plot_coverage_graphic(self):
        list_of_distance_covered = []
        list_of_routes_used = []
        list_of_used_edges = []
        new_value_distance_covered = 0.0
        routes_used = 0
        while True:
            route_path = list(self.routes.keys())
            route_path.sort(key= lambda a: self.routes[a].total_distance, reverse = True)
            greater_route = self.routes[route_path.pop(0)]
            if greater_route.total_distance == 0.0:
                break
            for edge in greater_route.get_edges_useds():
                if edge not in list_of_used_edges:
                    new_value_distance_covered = new_value_distance_covered + edge.distance
                    list_of_used_edges.append(edge)

            for edge in list_of_used_edges:
                edge.distance = 0.0
            self.recalculate_routes()
            list_of_distance_covered.append(new_value_distance_covered/self.total_distance)
            routes_used = routes_used + 1
            list_of_routes_used.append(routes_used)
        plt.plot(list_of_routes_used, list_of_distance_covered)
        plt.show()
        return

    def add_path(self, edge, path_id):
        if path_id not in self.routes.keys():
            self.routes[path_id] = Route(path_id)
        self.routes[path_id].add_edge_to_path(edge)
        return

    def recalculate_routes(self):
        for route in self.routes.keys():
            self.routes[route].recalculate_distance()
        return


class GraphDualSided:

    def __init__(self):  # inicializando grafo direcionado
        self.qtd_highways = 0
        self.nodes = {}
        self.edges = {}
        self.total_distance = 0.0
        self.routes = {}
        return

    def add_node(self, node_id, long, lat):  # adiciona um node no grafo
        new_node = NodeDualSided(node_id, long, lat)
        self.nodes[node_id] = new_node
        return

    def add_edge(self, source_id, target_id, distance, direction):  # adiciona uma edge no grafo e cria uma outra edge paralela na direcao inversa
        if direction == 'I':  # criando edge de ida
            source = self.nodes[source_id]
            target = self.nodes[target_id]
            new_edge = EdgeDualSided(source, target, distance)
            source.add_edge(new_edge)  # adicionando edge nos nodes que sao conectados por ele
            target.add_edge(new_edge)
            self.edges[new_edge.id] = new_edge
        else:  # criando edge de volta
            target = self.nodes[source_id]
            source = self.nodes[target_id]
            new_edge = EdgeDualSided(source, target, distance)
            source.add_edge(new_edge)
            target.add_edge(new_edge)
            self.edges[new_edge.id] = new_edge
        self.total_distance = self.total_distance + float(distance)
        return new_edge

    def add_path(self, edge, path_id):  # adiciona um edge em uma rota especifica
        if path_id not in self.routes.keys():
            self.routes[path_id] = Route(path_id)
        self.routes[path_id].add_edge_to_path(edge)
        return self.routes[path_id]

    def recalculate_routes(self):  # calculando quanto de cada edge ainda nao foi coberta pela rede
        for route in self.routes.keys():
            self.routes[route].recalculate_distance()
        return

    def plot_coverage_graphic(self, ida_e_volta=False, plot = True):
        list_of_distance_covered = []
        list_of_routes_used = []
        list_of_used_edges = []
        new_value_distance_covered = 0.0
        routes_used = []
        while True:  # algoritmo ira rodar ate a maior rota disponivel cobrir 0 de espaco
            routes_using = []
            route_path = list(self.routes.keys())
            route_path.sort(key = lambda a: self.routes[a].total_distance, reverse = True)
            route_id = route_path.pop(0)
            greater_route = self.routes[route_id]
            if greater_route.total_distance == 0.0:
                break  # fim do loop pois a rota que cobrir mais nao consiguira cobrir nada novo
            for edge in greater_route.get_edges_useds():
                if edge not in list_of_used_edges:
                    new_value_distance_covered = new_value_distance_covered + edge.distance
                    list_of_used_edges.append(edge)
            routes_using.append(greater_route)  # adicionando rota que mais cobre novas ruas a lista de rotas
            if ida_e_volta:  # se for ser considerado ida e volta de uma vez ele ira realizar o processo com o caminho inverso do encontrado
                if '(I)' in route_id:  # se for uma rota de ida ele ira realizar a volta
                    if route_id[:-3] + '(V)' in self.routes.keys():
                        for edge in self.routes[route_id[:-3] + '(V)'].get_edges_useds():
                            if edge not in list_of_used_edges:
                                new_value_distance_covered = new_value_distance_covered + edge.distance
                                list_of_used_edges.append(edge)
                        routes_using.append(self.routes[route_id[:-3] + '(V)'])
                else:  # se for uma rota de volta ele ira realizar a ida
                    if route_id[:-3] + '(I)' in self.routes.keys():
                        for edge in self.routes[route_id[:-3] + '(I)'].get_edges_useds():
                            if edge not in list_of_used_edges:
                                new_value_distance_covered = new_value_distance_covered + edge.distance
                                list_of_used_edges.append(edge)
                        routes_using.append(self.routes[route_id[:-3] + '(I)'])
            for edge in list_of_used_edges:  # zerando todas as edges que ja foram percorridas
                edge.distance = 0.0
            self.recalculate_routes()  # reorganizando a lista de rotas de acordo com o tamanho de caminhos nao cobertos
            list_of_distance_covered.append(new_value_distance_covered / self.total_distance)
            routes_used.append(routes_using)
            list_of_routes_used.append(len(routes_used))
        if plot:  # plotando grafico de rotas usadas por distancia coberta
            plt.plot(list_of_routes_used, list_of_distance_covered)
            plt.show()
        return routes_used  # retornando todas as rotas/linhas de onibus usadas para cobrir todas as edges do grafo
