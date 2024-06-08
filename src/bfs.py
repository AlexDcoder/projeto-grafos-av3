from math import inf
from grafo import Plataforma, Video


def BFS(plataforma: Plataforma, video_inicial: Video):
    n = plataforma.get_length()
    color = ["WHITE"] * n
    d = [inf] * n
    pi = [-1] * n

    s = plataforma.videos.index(video_inicial)

    color[s] = "GRAY"
    d[s] = 0

    Q = []
    Q.append(plataforma.videos[s])
    while len(Q) > 0:
        u = Q.pop(0)
        for v in u.relacionados:
            index_v = plataforma.videos.index(v)
            if color[index_v] == "WHITE":
                color[index_v] = "GRAY"
                d[index_v] = d[plataforma.videos.index(u)] + 1
                pi[index_v] = u
                Q.append(v)
    return d, pi
