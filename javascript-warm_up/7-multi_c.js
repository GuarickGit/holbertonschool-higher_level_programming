#!/usr/bin/node

const args = process.argv.slice(2);
const stringToPrint = 'C is fun';
const numberOfOccurences = parseInt(args[0]);

if (isNaN(numberOfOccurences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberOfOccurences; i++) {
    console.log(stringToPrint);
  }
}
