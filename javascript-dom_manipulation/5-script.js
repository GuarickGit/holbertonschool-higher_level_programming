#!/usr/bin/node

const element = document.getElementById('update_header');
const headerElement = document.querySelector('header');

element.addEventListener('click', function () {
  headerElement.textContent = 'New Header!!!';
});
