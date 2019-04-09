

def split_file(path, path2, path3):
    file = open(path, 'r', encoding = 'utf-8')  # pasta origem
    map_node = open(path2, 'w', encoding = 'utf-8')  # pasta destido dos nodes
    map_way = open(path3, 'w', encoding = 'utf-8')  # pasta destino das ruas
    mode = False
    for line in file.readlines():
        if '<node id' in line:
            map_node.write(line)
            continue
        if '<way' in line:
            map_way.write(line)
            mode = True
        if mode:
            if '<tag' in line:
                map_way.write(line)
            if '<nd' in line:
                map_way.write(line)
    file.close()
    map_node.close()
    map_way.close()
    return
