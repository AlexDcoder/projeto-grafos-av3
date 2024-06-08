"""
    Bibliotecas Python
"""
import json
from pprint import pprint
from random import randint

QTD_VIDEOS = 10
_titulos_videos: list[str] = []
_thumbnails: list[str] = []
_autores: list[str] = []
_likes: list[int] = []

videos: dict = {
    f"video {num + 1}":
    {
        "titulo": f"algum título {num + 1}",
        "autor": f"algum nome {num + 1}",
        "likes": randint(1, 10000),
        "thumbnail": f"alguma thumbnail {num + 1}"
    }
        for num in range(QTD_VIDEOS)
}

pprint(videos)

# TODO criar nova ideia para colocar grafos como centro do projeto
# TODO tomar como base os nomes dos criadores para criar o algoritmo
# TODO alterar o front com base no backend
# TODO SALVAR OS DADOS COM BASE NO VÍDEO ESCOLHIDO
