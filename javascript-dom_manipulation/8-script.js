#!/usr/bin/node

// On attend que le contenu HTML de la page soit entièrement chargé
// Cela permet d'accéder aux éléments du DOM comme le <div id="hello">
document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')

    .then(response => response.json())
    .then(data => {
      const helloDiv = document.getElementById('hello');

      helloDiv.textContent = data.hello;
    });
});
