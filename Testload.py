import GraphImporter
import GraphPainter
import MapImporter
import MapColapser
from Graph import GraphDualSided
import FileSpliter


lanes_types = ['primary', 'motorway']  # definindo qual os tipos de ruas do openstreet map sao consideradas importantes

my_graph = GraphDualSided()  # criando um grafo das paradas de onibus

GraphImporter.import_graph_dual_sided(my_graph, 'bus-network.txt')  # inicializando o grafo com os dados importados do txt

routes_used = my_graph.plot_coverage_graphic(ida_e_volta = True, plot = False)  # calcula quantas linhas sao necessarias para preencher o grafo

quant = int(input('Com quais primeiras linhas deseja montar o grafo?\n'))

FileSpliter.split_file('map.txt', 'map_node.txt', 'map_way.txt')  # separando o arquivo do openstreetmap para facilitar leitura posteriormente

node_dicts = MapImporter.node_importer('map_node.txt')  # criando lista de nodes apartir dos nodes do OpenStreetMap

ways_dicts = MapImporter.way_importer('map_way.txt', lanes_types, node_dicts)  # criando lista de ruas importantes composta de nodes do openstreetmap

MapColapser.compare_and_find_streets(my_graph, ways_dicts, first_found = True)  # procurando em que rua as paradas de onibus estao comparando lat e long do grafo de paradas e das rotas do openstreetmap

G = GraphPainter.draw_graph(routes_used, quant, my_graph.qtd_highways, plot = True)  # desenhando grafo final com rotas que estao em ruas principais com cor diferentes e calculando cobertura
                                                                                     # alcancada com a quantidade de rotas selecionada(sao consideradas apenas ruas principais que sao possiveis
                                                                                     # serem alcancadas com onibus)

