from math import inf

# Algoritmo de busca em profundidade


def BFS(n, network, s):
    color = ["WHITE"]*n
    d = [inf]*n
    pi = [-1]*n

    color[s] = "GRAY"
    d[s] = 0

    Q = []
    Q.append(s)
    while len(Q) > 0:
        u = Q.pop(0)
        for v in range(n):
            if network[u][v] > 0 and color[v] == "WHITE":
                color[v] = "GRAY"
                d[v] = d[u]+1
                pi[v] = u
                Q.append(v)
    return d, pi
