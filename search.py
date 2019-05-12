def breadth_first_search(graph, start):
    ''' Returns a list of 
    '''
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(set(graph[node]) - visited)
    return list(visited)