#!/usr/bin/node

const element = document.getElementById('toggle_header');
const headerElement = document.querySelector('header');

element.addEventListener('click', function () {
  if (headerElement.classList.contains('red')) {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else if (headerElement.classList.contains('green')) {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});
