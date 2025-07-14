#!/usr/bin/node

const element = document.getElementById('red_header');
const elementToRetrieve = document.querySelector('header');

element.addEventListener('click', function () {
  elementToRetrieve.style.color = '#FF0000';
});
