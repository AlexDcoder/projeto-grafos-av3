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