from copy import copy
from search import breadth_first_search

def __is_connected(graph):
    '''Checks if a graph is connected or not, using Breadth-First Search Algorithm (BFS)
    @type graph: dict
    @param graph: The graph
    @rtype: bool
    '''
    node_start = list(graph)[0]
    bfs_list = breadth_first_search(graph, node_start)
    return len(bfs_list) == len(graph)

def __odd_degree_nodes(graph):
    ''' Returns a list of all odd degrees nodes from a graph
    @type graph: dict
    @param graph: The graph
    @rtype: list
    @returns: all odd degree nodes in graph
    '''
    odd_degree_nodes = []
    for node in graph:
        if len(graph[node]) % 2 != 0: # if node degree is even
            odd_degree_nodes.append(node)
    return odd_degree_nodes

def __from_dict(graph):
    ''' Return a list of tuples edges from a graph in a dictionary format
    @type graph: dict
    @param graph: The graph
    @rtype: list of tuples
    @returns: all edges in graph
    '''    
    links = []
    for node in graph:
        for node_next in graph[node]:
            links.append((node,node_next)) # append edge u,v (node, node_next)
    return links


def fleury(graph = dict()):
    ''' Gets and returns the eulerian graph from one given graph
    @type graph: dict
    @param graph: The graph
    @rtype: list of tuples
    @returns: eulerian path in graph
    '''
    odn = __odd_degree_nodes(graph)
    if len(odn) > 2 or len(odn) == 1:
        return 'Not Eulerian Graph'
    else:
        graph_copy = copy(graph)
        trail = []
        if len(odn) == 2:
            node = odn[0]
        else:
            node = list(graph_copy)[0]
        while __from_dict(graph_copy): # edges amount greater 0
            current_node = node
            for node in graph_copy[current_node]:
                graph_copy[current_node].remove(node)
                graph_copy[node].remove(current_node)
                bridge = not __is_connected(graph_copy)
                if bridge:
                    graph_copy[current_node].append(node)
                    graph_copy[node].append(current_node)
                else:
                    break
            if bridge:
                graph_copy[current_node].remove(node)
                graph_copy[node].remove(current_node)
                graph_copy.pop(current_node)
            trail.append((current_node, node))
    return trail