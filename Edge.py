class Edge:  # classe nao usada
    def __init__(self, nodes, distance, edge_id):
        self.id = edge_id
        self.nodes = nodes
        self.distance = distance
        return


class EdgeDualSided:
    def __init__(self, source, target, distance):
        self.routes = {}  # lista de rotas que utilizam essa edge no caminho
        self.id = source.id + '->' + target.id
        self.source = source
        self.target = target
        self.distance = distance  # distancia que a edge cobre da rede
        return

    def add_path(self, route):  # adiciona nova rota que utiliza essa edge
        self.routes[route.route_id] = route
        return
