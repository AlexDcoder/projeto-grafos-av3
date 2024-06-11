# Criação do modelo de grafo

PESO_TAG, PESO_AUTOR, PESO_LIKE = 20, 200, 1


class Video:
    '''
        Criando vértice que representa o vídeo
    '''

    def __init__(
            self, id: str, title: str, autor: str, tags: set[str], likes: int,
            thumbnail: str = "", icon: str = "",
            views: str = "", time_posted: str = "") -> None:
        self.id = id
        self.title: str = title
        self.autor: str = autor
        self.thumbnail: str = thumbnail
        self.icon: str = icon
        self.views: str = views
        self.time_posted: str = time_posted
        self.tags: set = tags
        self.likes: int = likes
        self.relacionados: list = []

    def nivel_de_similaridade(self, outro_video) -> int:
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

    def __repr__(self) -> str:
        return f"(Autor: {self.autor},\nTags: {self.tags},\n"\
            f"Likes: [{self.likes}]), Relacionados: {self.relacionados}"


class Plataforma:
    '''
        Criando grafo da plataforma
    '''

    def __init__(self) -> None:
        self.videos: list[Video] = []

    def adicionando_video_a_plataforma(self, video):
        '''
            Adiocionar vídeos à plataforma
        '''
        self.videos.append(video)

    def relacionar_videos(self, video1, video2):
        '''
            Relacionar dois vídeos na plataforma
        '''
        index_video_1 = self.videos.index(video1)
        index_video_2 = self.videos.index(video2)

        self.videos[index_video_1].relacionados.append(
            self.videos[index_video_2])

    def get_length(self):
        return len(self.videos)
