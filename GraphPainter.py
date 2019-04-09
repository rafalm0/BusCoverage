import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(routes_used, quant=50, qtd_highways=0, with_pos=True, plot=True):
    nodes_added = []
    G = nx.Graph()
    color_map = []
    x = 0
    if with_pos:  # sempre que possivel usar with_pos = True
        for route in routes_used:
            for semiroute in route:
                for edge in semiroute.path.keys():
                    rua = semiroute.path[edge]
                    if rua.source not in nodes_added:
                        if rua.source.street_name != '':
                            x += 1
                            color_map.append('blue')
                        else:
                            color_map.append('red')
                        G.add_node(rua.source.id.split('p_')[1], pos = (rua.source.long, rua.source.lat))
                        nodes_added.append(rua.source)
                    if rua.target not in nodes_added:
                        if rua.source.street_name != '':
                            color_map.append('blue')
                            x += 1
                        else:
                            color_map.append('red')
                        G.add_node(rua.target.id.split('p_')[1], pos = (rua.target.long, rua.target.lat))
                        nodes_added.append(rua.target)
                    G.add_edge(rua.source.id.split('p_')[1], rua.target.id.split('p_')[1])

            quant = quant - 1
            if quant == 0:
                break  # quando alcancar a quantidade desejada de rotas sera saido do loop e o grafo sera desenhado
        print("desenhando grafo...")
        pos = nx.get_node_attributes(G, 'pos')
        if not qtd_highways == 0:
            print(x / qtd_highways)  # porcentagem de ruas principais coberta com configuracao atual do grafos de rotas de onibus
        if plot:
            nx.draw(G, pos, with_labels = False, node_color = color_map, font_weight = 'bold', node_size = 15)
            plt.show()
    else:  # metodo nao utilizado pois nao cria um grafo com coordenadas(dificultado visualizacao)
        for route in routes_used:
            for semiroute in route:
                for edge in semiroute.path.keys():
                    rua = semiroute.path[edge]
                    G.add_node(rua.source.id.split('_')[1])
                    G.add_node(rua.target.id.split('_')[1])
                    G.add_edge(rua.source.id.split('_')[1], rua.target.id.split('_')[1])
            quant = quant - 1
            if quant == 0:
                break
        print("desenhando grafo...")
        if plot:
            nx.draw(G, with_labels = False, font_weight = 'bold')
            plt.show()

    return G
