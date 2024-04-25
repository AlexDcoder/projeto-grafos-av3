# Criação do modelo de grafo

# PESAGEM
# TAG: 20
# QTD LIKES: 1
# CRIADOR: 200

class Video:
    def __init__(self, autor, tag, qtd_likes) -> None:
        self.autor: str = autor
        self.tag: str = tag
        self.qtd_likes: int = qtd_likes
        self.relacionados: list = []

    def add_video_relacionado(self, video1):
        if video1.tag == self.tag or video1.autor == self.autor:
            self.relacionados.append(video1)
            video1.relacionados.apped(self)


class Plataforma:
    def __init__(self) -> None:
        self.videos: list[Video] = []

    def adicionando_video_a_plataforma(self, video):
        self.videos.append(video)
