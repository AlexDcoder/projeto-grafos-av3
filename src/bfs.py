from math import inf
from src.grafo import Plataforma, Video
# Algoritmo de busca em profundidade


def BFS(plataforma: Plataforma, video_inicio: Video):
    color = ["WHITE"]*len(plataforma.videos)
    d = [inf]*len(plataforma.videos)
    pi = [-1]*len(plataforma.videos)

    color[plataforma.videos.index(video_inicio)] = "GRAY"
    d[plataforma.videos.index(video_inicio)] = 0

    # Q = []
    # Q.append(s)
    # while len(Q) > 0:
    #     u = Q.pop(0)
    #     for v in range(n):
    #         if plataforma[u][v] > 0 and color[v] == "WHITE":
    #             color[v] = "GRAY"
    #             d[v] = d[u]+1
    #             pi[v] = u
    #             Q.append(v)
    return d, pi
