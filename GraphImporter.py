

def import_graph(graph, file_path):  # funcao nao utilizada no momento
    reading = 'nodes'
    file = open(file_path, 'r')

    for line in file:
        if line == 'nodes\n':
            reading = 'nodes'
        elif line == 'edges\n':
            reading = 'edges'
        else:
            in_line = line.split(',')
            if reading == 'nodes':
                graph.add_node(in_line[0])
            else:
                edge_created = graph.add_edge(in_line[4].strip(), [in_line[0], in_line[2]])
                if ',;' in line:
                    for route in line.split(',;')[1].split('\n')[0].split(';'):
                        graph.add_path(edge_created, route)
                else:
                    for route in line.split(',lines,')[1].split(';')[:-1]:
                        graph.add_path(edge_created, route)
    return


def import_graph_dual_sided(graph, file_path):
    reading = 'nodes'
    file = open(file_path, 'r')

    for line in file:
        if line == 'nodes\n':
            reading = 'nodes'
        elif line == 'edges\n':
            reading = 'edges'
        else:
            in_line = line.split(',')
            if reading == 'nodes':
                graph.add_node(in_line[0], float(in_line[6].rstrip()), float(in_line[8].rstrip()))  # adicionando node no grafo
            else:
                if ',;' in line:
                    for route in line.split(',;')[1].split('\n')[0].split(';'):  # preparando para adicionar rotas em cada edge
                        if route == '':
                            continue
                        if route.split('(')[1].split(')')[0] == 'I':
                            edge_created = graph.add_edge(in_line[0], in_line[2], float(in_line[4]), 'I')
                            edge_created.add_path(graph.add_path(edge_created, route))
                        else:
                            edge_created = graph.add_edge(in_line[0], in_line[2], float(in_line[4]), 'V')
                            edge_created.add_path(graph.add_path(edge_created, route))
                else:
                    for route in line.split(',lines,')[1].split(';')[:-1]:
                        if route.split('(')[1].split(')')[0] == 'I':
                            edge_created = graph.add_edge(in_line[0], in_line[2], float(in_line[4]), 'I')
                            edge_created.add_path(graph.add_path(edge_created, route))
                        else:
                            edge_created = graph.add_edge(in_line[0], in_line[2], float(in_line[4]), 'V')
                            edge_created.add_path(graph.add_path(edge_created, route))
    graph.recalculate_routes()  # usando funcao para atribuir valores iniciais a cada rota
    return










