var sanduiche = document.querySelector(".menu-sanduiche");
var sidebars = document.querySelectorAll(".sidebar");
var videoAreas = document.querySelectorAll(".video-container");
var filtros = document.querySelectorAll(".filtros");

var inscricoes = document.querySelectorAll(".inscricoes");
var explorar = document.querySelectorAll(".explorar");
var maisYT = document.querySelectorAll(".mais-youtube");
var config = document.querySelectorAll(".configuracoes");
var final = document.querySelectorAll(".final");
var linhas = document.querySelectorAll(".linha");
var videos = document.querySelectorAll(".video");

var outrosIcones = document.querySelector(".outros-icones");

sanduiche.onclick = function () {
  // Itera sobre todos os elementos encontrados com a classe e aplica as alterações
  sidebars.forEach(function (sidebar) {
    sidebar.classList.toggle("small-sidebar");
  });
  videoAreas.forEach(function (videoArea) {
    videoArea.classList.toggle("aumenta-video-container");
  });
  filtros.forEach(function (filtro) {
    filtro.classList.toggle("small-filtros");
  });
  inscricoes.forEach(function (inscricao) {
    inscricao.classList.toggle("esconde-inscricoes");
  });
  explorar.forEach(function (itemExplorar) {
    itemExplorar.classList.toggle("esconde-explorar");
  });
  maisYT.forEach(function (itemMaisYT) {
    itemMaisYT.classList.toggle("esconde-mais-youtube");
  });
  config.forEach(function (itemConfig) {
    itemConfig.classList.toggle("esconde-configuracoes");
  });
  final.forEach(function (itemFinal) {
    itemFinal.classList.toggle("esconde-final");
  });
  linhas.forEach(function (linha) {
    linha.classList.toggle("esconde-linha");
  });
  videos.forEach(function (video) {
    video.classList.toggle("aumenta-video");
  });
  outrosIcones.classList.toggle("esconde-outros-icones");
}

document.addEventListener("DOMContentLoaded", function () {
  var videos = document.querySelectorAll(".video");
  videos.forEach(function (video) {
      video.addEventListener("click", function () {
          var videoId = this.getAttribute("data-id");
          realizarCalculo(videoId);
      });
  });
});

function realizarCalculo(videoId) {
  fetch(`/realizar_calculo/${videoId}`)
      .then(response => response.json())
      .then(data => {
          if (data.error) {
              console.error(data.error);
              return;
          }
          console.log(data); 
          mostrarResultados(data);
      })
      .catch(error => console.error('Error:', error));
}

function mostrarResultados(resultados) {
  var resultadosContainer = document.getElementById("resultados");
  resultadosContainer.innerHTML = "";

  resultados.forEach(function (resultado) {
      var videoDiv = document.createElement("div");
      videoDiv.classList.add("video");

      var thumbnail = document.createElement("img");
      thumbnail.src = resultado.thumbnail;
      thumbnail.classList.add("thumbnail");

      var videoDetalhes = document.createElement("div");
      videoDetalhes.classList.add("video-detalhes");

      var icon = document.createElement("img");
      icon.src = resultado.icon;
      icon.classList.add("icone-canal");

      var infoVideo = document.createElement("div");
      infoVideo.classList.add("info-video");

      var tituloVideo = document.createElement("h4");
      tituloVideo.classList.add("titulo-video");
      tituloVideo.innerText = resultado.title;

      var nomeCanal = document.createElement("p");
      nomeCanal.classList.add("nome-canal");
      nomeCanal.innerText = resultado.autor;

      var videoViews = document.createElement("p");
      videoViews.classList.add("video-views");
      videoViews.innerText = `${resultado.views} . ${resultado.time_posted}`;

      infoVideo.appendChild(tituloVideo);
      infoVideo.appendChild(nomeCanal);
      infoVideo.appendChild(videoViews);

      videoDetalhes.appendChild(icon);
      videoDetalhes.appendChild(infoVideo);

      videoDiv.appendChild(thumbnail);
      videoDiv.appendChild(videoDetalhes);

      resultadosContainer.appendChild(videoDiv);
  });
}
