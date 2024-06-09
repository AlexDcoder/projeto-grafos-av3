from math import inf
from grafo import Plataforma, Video
from random import randint
from copy import deepcopy


def BFS(plataforma: Plataforma, video_inicial: Video):
    n = plataforma.get_length()
    color = ["WHITE"] * n
    d = [inf] * n
    pi = [-1] * n
    pesos = [0] * n
    s = plataforma.videos.index(video_inicial)

    color[s] = "GRAY"
    d[s] = 0

    Q = []
    Q.append(plataforma.videos[s])

    while len(Q) > 0:
        u = Q.pop(0)
        for v in plataforma.videos:
            index_v = plataforma.videos.index(v)
            if v != u and color[index_v] == "WHITE" and \
                    plataforma.videos[index_v].nivel_de_similaridade(u) > 0:
                color[index_v] = "GRAY"
                d[index_v] = d[plataforma.videos.index(u)] + 1
                pi[index_v] = u
                pesos[index_v] = v.nivel_de_similaridade(u)
                Q.append(v)
            color[index_v] == "BLACK"
    return d, pi, pesos
