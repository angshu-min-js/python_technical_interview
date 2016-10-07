from random import randint

def edge(x, y):
    return (x, y) if x < y else (y, x)

def poprandom(nodes):
    x_i = randint(0, len(nodes) - 1)
    return nodes.pop(x_i)

def pickrandom(nodes):
    x_i = randint(0, len(nodes) - 1)
    return nodes[x_i]

def check_nodes(x, nodes, tour):
    for i, n in enumerate(nodes):
        t = edge(x, n)
        if t not in tour:
            tour.append(t)
            nodes.pop(i)
            return n
    return None

def create_tour(nodes):
    connected = []
    degree = {}
    unconnected = [n for n in nodes]
    tour = []
    # create a connected graph
    # first, pick two random nodes for an edge
    x = poprandom(unconnected)
    y = poprandom(unconnected)
    connected.append(x)
    connected.append(y)
    tour.append(edge(x,y)) 
    degree[x] = 1
    degree[y] = 1
    # then, pick a random node from the unconnected
    # list and create an edge to it
    while len(unconnected) > 0:
        x = pickrandom(connected)
        y = poprandom(unconnected)
        connected.append(y)
        tour.append(edge(x, y))
        degree[x] += 1
        degree[y] = 1
    # now make sure each node has an even degree.
    # have the problem of not adding a duplicate edge
    odd_nodes = [k for k, v in degree.items() if v % 2 == 1]
    even_nodes = [k for k, v in degree.items() if v % 2 == 0]
    # there will always be an even number of odd nodes
    # (hint: the sum of degrees of a graph is even)
    # so we can just connect pairs of unconnected edges
    while len(odd_nodes) > 0:
        x = poprandom(odd_nodes)
        cn = check_nodes(x, odd_nodes, tour)
        if cn is not None:
            even_nodes.append(x)
            even_nodes.append(cn)
        else:
            # if we get here
            # the node is already connected to
            # all the odd nodes so we need to find an 
            # even one to connect to
            cn = check_nodes(x, even_nodes, tour)
            # cn cannot be None, and needs to be
            # added to the odd_nodes list
            odd_nodes.append(cn)
            # but, x is now an even node
            even_nodes.append(x)
    return tour