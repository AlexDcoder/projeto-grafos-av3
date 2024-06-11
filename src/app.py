from flask import Flask, render_template, request, redirect, url_for, jsonify
from grafo import Plataforma, Video
from bfs import BFS
from random import randint
import json
from copy import deepcopy

with open("../videos.json", encoding="utf-8") as db_file:
    videos_data = json.load(db_file)

plataforma = Plataforma()
videos_dict = {}

for video_data in videos_data:
    video = Video(
        id=video_data["id"],
        title=video_data["title"],
        autor=video_data["channel_name"],
        tags=set(video_data["tags"]),
        likes=randint(10, 1000),
        thumbnail=video_data["thumbnail"],
        icon=video_data["channel_icon"],
        views=video_data["views"],
        time_posted=video_data["time_ago"]
    )
    plataforma.adicionando_video_a_plataforma(video)
    videos_dict[video_data["id"]] = video

app = Flask(__name__, template_folder='../templates',
            static_folder='../static')


@ app.route('/')
def home():
    '''
        Página inicial do Ustube
    '''
    return render_template("index.html", videos=videos_data)


@app.route('/<video_id>')
def realizar_calculo(video_id):
    video_inicial = videos_dict.get(video_id)
    if not video_inicial:
        return jsonify({"error": "Video not found"}), 404

    _, pesos = BFS(plataforma, video_inicial)
    pesos_sorteados = sorted(pesos, key=lambda x: x[1], reverse=True)
    print(pesos_sorteados[0][0].id)
    resultados = []

    for v in pesos_sorteados:
        resultados.append({
            "id": v[0].id,
            "thumbnail": v[0].thumbnail,
            "icon": v[0].icon,
            "title": v[0].title,
            "autor": v[0].autor,
            "views": v[0].views,
            "time_posted": v[0].time_posted,
        })

    return render_template("result.html", resultados=resultados)


if __name__ == "__main__":
    app.run(debug=True)
