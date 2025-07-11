#!/usr/bin/node

const args = process.argv.slice(2);
const characterToPrint = 'X';
const size = parseInt(args[0]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = ''; // Reset row à chaque tour
    for (let j = 0; j < size; j++) {
      row += characterToPrint;
    }
    console.log(row);
  }
}
