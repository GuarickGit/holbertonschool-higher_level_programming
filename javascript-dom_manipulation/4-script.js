#!/usr/bin/node

const element = document.getElementById('add_item');
const ulElement = document.querySelector('ul');

element.addEventListener('click', function () {
  const list = document.createElement('li');
  list.textContent = 'Item';
  ulElement.appendChild(list);
});
