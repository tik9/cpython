graph = {'A': ['B', 'C'],
        'B': ['A', 'F'],
        'C': ['D', 'E'],
        'D': ['H', 'C'],
        'E': ['C', 'F'],
        'F': ['B', 'G'],
        'G': ['F', 'H'],
        'H': ['G', 'D', ],
}

viewed_nodes = []

def main():
    '''main'''
    for node in graph:
        traverse(node)

    print(sorted(viewed_nodes))


def traverse(into):
    '''depth'''
    if into in viewed_nodes:
        return

    viewed_nodes.append(into)

    for outto in graph[into]:
        if outto not in viewed_nodes:
            traverse(outto)


if __name__=='__main__':
    main()