#!/usr/bin/node

const element = document.getElementById('red_header');
const headerElement = document.querySelector('header');

element.addEventListener('click', function () {
  headerElement.classList.add('red');
});
