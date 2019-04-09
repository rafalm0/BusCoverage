class Route:
    def __init__(self, path_id):
        self.total_distance = 0.0
        self.route_id = path_id
        self.path = {}
        return

    def add_edge_to_path(self, edge):
        self.path[edge.id] = edge
        return

    def recalculate_distance(self):
        new_distance = 0.0
        for edge in self.path.keys():
            new_distance = new_distance + self.path[edge].distance
        # if self.total_distance != new_distance:
        #     print()
        self.total_distance = new_distance
        return

    def get_edges_useds(self):
        lista = []
        for edge in self.path.keys():
            lista.append(self.path[edge])
        return lista
