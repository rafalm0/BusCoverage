

def compare_and_find_streets(my_graph, streets_dict, first_found = False):
    """" first_found faz com que a primeira rua com uma proximidade de 0.0005 em longitude e latitude ja seja selecionada como a rua que contem aquela parada de onibus
         caso contrario sempre sera procurado a rua mais proxima possivel(mesmo que seja a mesma rua em outro ponto) dentre todos os nodes do mapa do openstreetmap
         isso e realizado para todos os nodes do grafo das paradas de onibus, procurando oem qual rua aquela parada esta contida
    """""
    for graph_node in my_graph.nodes:
        node = my_graph.nodes[graph_node]
        for route in streets_dict:
            for route_node in streets_dict[route]:
                lat_dif = abs(node.lat - route_node['lat'])
                long_dif = abs(node.long - route_node['long'])
                if (lat_dif > 0.0005) or (long_dif > 0.0005):
                    continue
                else:
                    if (lat_dif < node.street_lat) and (long_dif < node.street_long):
                        node.street_lat = lat_dif
                        node.street_long = long_dif
                        node.street_name = route
                        if first_found:
                            break
            else:
                continue
            break
    for graph_node in my_graph.nodes:
        node = my_graph.nodes[graph_node]
        if node.street_name != '':
            my_graph.qtd_highways += 1  # quantidade de nodes em ruas encontrados ao total, futuramente usado para calcular quanto de corbertura e alcancavel com uma quantidade especifica de rotas
    return
