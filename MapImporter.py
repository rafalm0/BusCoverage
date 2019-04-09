

def node_importer(path):
    nodes = {}
    file = open(path, 'r', encoding = 'utf-8')
    for line in file.readlines():
        splited_line = line.split('=')
        nodes[splited_line[1].split('"')[1]] = {'long': float(splited_line[3].split('"')[1]), 'lat': float(splited_line[2].split('"')[1]), 'rua': ''}
    return nodes


def way_importer(path, lanes_accepted, node_dict):
    ways = {}
    file = open(path, 'r', encoding = 'utf-8')
    list_of_nodes = []
    way_name = ''
    highway = False
    for line in file.readlines():
        if '</way' in line:
            if highway:  # rua era highway e pode adicionar nas ruas importantes
                if (way_name != '') and (way_name != 'Ligação á BR-166') and (way_name != 'Pista Marginal'):  # removendo duas ruas que geravam problema

                    if way_name not in ways.keys():
                        ways[way_name] = list_of_nodes
                    else:
                        new_list = ways[way_name]
                        for node in list_of_nodes:
                            new_list.append(node)
                        ways[way_name] = new_list
            highway = False
            list_of_nodes = []
            way_name = ''
        if '<nd ref' in line:
            list_of_nodes.append(node_dict[line.split('"')[1]])  # adicionando os nodes as ruas
        if '<tag' in line:
            if '"name"' in line:
                way_name = line.split('"')[3]  # atribuindo nome das ruas
            elif '"highway"' in line:
                lane_type = line.split('"')[3]  # verificando tipo da rua
                if lane_type in lanes_accepted:
                    highway = True  # se chegou ate aqui a rua analisando e considerada importante e prepara para em outra iteracao adicionar as rotas conhecidas
    return ways
