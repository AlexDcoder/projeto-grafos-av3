# Criação do modelo de grafo
# pode usar distância mínima, para criar cluster mínimo de vídeos
# add collabs

PESO_TAG, PESO_AUTOR, PESO_LIKE = 20, 200, 1


class Video:
    '''
        Criando vértice que representa o vídeo
    '''

    def __init__(self, autor: str, tags: set[str], likes: int) -> None:
        self.autor: str = autor
        self.tags: set = tags
        self.likes: int = likes
        self.relacionados: list = []

    def add_video_relacionado(self, outro_video):
        if outro_video.tags == self.tags or outro_video.autor == self.autor:
            self.relacionados.append(outro_video)
            outro_video.relacionados.apped(self)

    def nivel_de_similaridade(self, outro_video):
        '''
            Definindo um nível de similaridade entre vídeos
        '''
        similaridade_tags = len(self.tags.intersection(
            outro_video.tags)) / len(self.tags.union(outro_video.tags))

        similaridade_likes = 1 - \
            abs(self.likes - outro_video.likes) / \
            max(self.likes, outro_video.likes)

        similaridade_autor = 1 if self.autor == outro_video.autor else 0

        semelhanca_total = (similaridade_tags * PESO_TAG +
                            similaridade_likes * PESO_LIKE +
                            similaridade_autor * PESO_AUTOR)

        return semelhanca_total


class Plataforma:
    '''
        Criando grafo da plataforma
    '''

    def __init__(self) -> None:
        self.videos: list[Video] = []

    def adicionando_video_a_plataforma(self, video):
        self.videos.append(video)
