import json

# Lista de vídeos com informações extraídas do HTML, incluindo novas entradas
videos = [
    {
        "id": "1",
        "thumbnail": "template/img/moana.jpg",
        "channel_icon": "template/img/profilefilmes.png",
        "title": "Moana 2 | Teaser Oficial",
        "channel_name": "Cine Mundo",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Cinema"]
    },
    {
        "id": "2",
        "thumbnail": "template/img/maxresdefault.jpg",
        "channel_icon": "template/img/profilemusica.png",
        "title": "Os Melhores Rocks de Todos",
        "channel_name": "Music Channel",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Música"]
    },
    {
        "id": "3",
        "thumbnail": "template/img/jogos.jpg",
        "channel_icon": "template/img/profilejogos.png",
        "title": "NOVOS JOGOS DE 2024",
        "channel_name": "Game Masters",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Games"]
    },
    {
        "id": "4",
        "thumbnail": "template/img/esportes.jpg",
        "channel_icon": "template/img/profileesportes.png",
        "title": "FINAL DA COPA DO REI",
        "channel_name": "Arena Esportiva",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Esporte"]
    },
    {
        "id": "5",
        "thumbnail": "template/img/esportes2.webp",
        "channel_icon": "template/img/profileesportes.png",
        "title": "JOGOS DE HOJE LIBERTADORES",
        "channel_name": "Arena Esportiva",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Esporte"]
    },
    {
        "id": "6",
        "thumbnail": "template/img/filmes2.jpg",
        "channel_icon": "template/img/profilefilmes.png",
        "title": "MELHORES FILMES DA DÉCADA!",
        "channel_name": "Cine Mundo",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Cinema"]
    },
    # Novos vídeos adicionados
    {
        "id": "7",
        "thumbnail": "template/img/id7.png",
        "channel_icon": "template/img/profilefilmes.jpg",
        "title": "Inception (A Origem) - Trailer",
        "channel_name": "Cine Mundo",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Cinema"]
    },
    {
        "id": "8",
        "thumbnail": "template/img/id8.png",
        "channel_icon": "template/img/profilefilmes.jpg",
        "title": "Avengers: Endgame (Vingadores: Ultimato) - Trailer",
        "channel_name": "Cine Mundo",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Cinema"]
    },
    {
        "id": "9",
        "thumbnail": "template/img/id9.png",
        "channel_icon": "template/img/profilefilmes.jpg",
        "title": "The Lord of the Rings: The Fellowship of the Ring (O Senhor dos Anéis: A Sociedade do Anel) - Trailer",
        "channel_name": "Cine Mundo",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Cinema"]
    },
    {
        "id": "10",
        "thumbnail": "template/img/id10.png",
        "channel_icon": "template/img/profilefilmes.jpg",
        "title": "Interstellar - Trailer",
        "channel_name": "Cine Mundo",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Cinema"]
    },
    {
        "id": "11",
        "thumbnail": "template/img/id11.png",
        "channel_icon": "template/img/profilefilmes.jpg",
        "title": "The Matrix - Trailer",
        "channel_name": "Cine Mundo",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Cinema"]
    },
    {
        "id": "12",
        "thumbnail": "template/img/id12.png",
        "channel_icon": "template/img/profilefilmes.jpg",
        "title": "Internet o Filme | Teaser Oficial ",
        "channel_name": "Cine Mundo",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Cinema"]
    },
    {
        "id": "13",
        "thumbnail": "template/img/id13.jpeg",
        "channel_icon": "template/img/profilemusica.jpg",
        "title": "Explorando os Segredos da Teoria Musical",
        "channel_name": "Music Channel",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Música"]
    },
    {
        "id": "14",
        "thumbnail": "template/img/id14.png",
        "channel_icon": "template/img/profilemusica.jpg",
        "title": "Os Maiores Guitarristas de Todos os Tempos",
        "channel_name": "Music Channel",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Música"]
    },
    {
        "id": "15",
        "thumbnail": "template/img/id15.png",
        "channel_icon": "template/img/profilemusica.jpg",
        "title": "Como Criar uma Música do Zero: Passo a Passo",
        "channel_name": "Music Channel",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Música"]
    },
    {
        "id": "16",
        "thumbnail": "template/img/id16.png",
        "channel_icon": "template/img/profilemusica.jpg",
        "title": "A Evolução da Música Pop: Dos Anos 60 aos Dias Atuais",
        "channel_name": "Music Channel",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Música"]
    },
    {
        "id": "17",
        "thumbnail": "template/img/id17.png",
        "channel_icon": "template/img/profilemusica.jpeg",
        "title": "Curiosidades Sobre Instrumentos Musicais que Você Não Sabia",
        "channel_name": "Music Channel",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Música"]
    },
    {
        "id": "18",
        "thumbnail": "template/img/id18.png",
        "channel_icon": "template/img/profilemusica.jpeg",
        "title": "Entrevista com um Compositor: Processo Criativo e Inspirações",
        "channel_name": "Music Channel",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Música"]
    },
    {
        "id": "19",
        "thumbnail": "template/img/id19.jpg",
        "channel_icon": "template/img/profilejogos.jpg",
        "title": "Os 10 Melhores Jogos de Todos os Tempos!",
        "channel_name": "Game Masters",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Games"]
    },
    {
        "id": "20",
        "thumbnail": "template/img/id20.png",
        "channel_icon": "template/img/profilejogos.jpeg",
        "title": "Guia Completo: Como se Tornar um Pro Player",
        "channel_name": "Game Masters",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Games"]
    },
    {
        "id": "21",
        "thumbnail": "template/img/id21.png",
        "channel_icon": "template/img/profilejogos.jpg",
        "title": "Análise Profunda: História e Curiosidades de Skyrim",
        "channel_name": "Game Masters",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Games"]
    },
    {
        "id": "22",
        "thumbnail": "template/img/id22.png",
        "channel_icon": "template/img/profilejogos.jpg",
        "title": "Desafios Insanos no GTA V",
        "channel_name": "Game Masters",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Games"]
    },
    {
        "id": "23",
        "thumbnail": "template/img/id23.png",
        "channel_icon": "template/img/profilejogos.jpg",
        "title": "Detonado Zelda",
        "channel_name": "Game Masters",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Games"]
    },
    {
        "id": "24",
        "thumbnail": "template/img/id24.png",
        "channel_icon": "template/img/profilejogos.jpg",
        "title": "Top 10 Easter Eggs Mais Surpreendentes em Jogos!",
        "channel_name": "Game Masters",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Games"]
    },
    {
        "id": "25",
        "thumbnail": "template/img/id25.jpeg",
        "channel_icon": "Barcelona vs Real Madrid",
        "title": "Fla vs Flu 2018",
        "channel_name": "Arena Esportiva",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Esporte"]
    },
    {
        "id": "26",
        "thumbnail": "template/img/id26.png",
        "channel_icon": "template/img/profileesportes.jpeg",
        "title": "Vini JR vai ser Bola de Ouro?",
        "channel_name": "Arena Esportiva",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Esporte"]
    },
    {
        "id": "27",
        "thumbnail": "template/img/id27.png",
        "channel_icon": "template/img/profileesportes.jpeg",
        "title": "Top 10 Gols Mais Bonitos",
        "channel_name": "Arena Esportiva",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Esporte"]
    },
    {
        "id": "28",
        "thumbnail": "template/img/id28.png",
        "channel_icon": "template/img/profileesportes.jpg",
        "title": "Melhores defesas de Goleiros",
        "channel_name": "Arena Esportiva",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Esporte"]
    },
    {
        "id": "29",
        "thumbnail": "template/img/id29.png",
        "channel_icon": "template/img/profileesportes.jpg",
        "title": "Campeonato de Volei",
        "channel_name": "Arena Esportiva",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Esporte"]
    },
    {
        "id": "30",
        "thumbnail": "template/img/id30.png",
        "channel_icon": "template/img/profileesportes.jpg",
        "title": "Melhores Enterradas da NBA",
        "channel_name": "Arena Esportiva",
        "views": "100 visualizações",
        "time_ago": "há 2 dias",
        "tags": ["Esporte"]
    },

]

# Converte a lista de vídeos para JSON
videos_json = json.dumps(videos, indent=4, ensure_ascii=False)

# Salva o JSON em um arquivo
with open('videos.json', 'w', encoding='utf-8') as f:
    f.write(videos_json)

print(videos_json)
