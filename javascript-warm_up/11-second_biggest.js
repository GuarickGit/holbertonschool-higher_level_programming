#!/usr/bin/node

// Récupère les arguments passés en ligne de commande (à partir du 3e élément).
const args = process.argv.slice(2);

// Si aucun argument ou un seul, il ne peut pas y avoir de 2e plus grand → afficher 0 et sortir.
if (args.length === 0 || args.length === 1) {
  console.log(0);
  process.exit(0);
}

// Convertit tous les arguments en nombres.
// map() permet de transformer chaque élément du tableau.
// Number(arg) convertit la chaîne de caractères en entier.
const numbers = args.map(arg => Number(arg));

// Pour trouver les plus grandes valeurs uniques, on veut ignorer les doublons.
// Set est une structure qui stocke uniquement des valeurs uniques.
// En le convertissant à nouveau en tableau avec [...set], on récupère un tableau sans doublons.
const uniqueNumbers = [...new Set(numbers)];

// On trie le tableau en ordre décroissant (du plus grand au plus petit).
// La méthode sort() trie par défaut par ordre alphabétique (utile pour des chaînes).
// Ici on fournit une fonction de comparaison pour trier des nombres correctement.
// b - a → trie du plus grand au plus petit.
uniqueNumbers.sort((a, b) => b - a);

// On vérifie à nouveau si, après suppression des doublons, on a encore au moins deux valeurs distinctes.
// Si ce n’est pas le cas, on affiche 0 et on quitte le programme.
if (uniqueNumbers.length < 2) {
  console.log(0);
  process.exit(0);
}

// Enfin, on affiche le deuxième plus grand nombre, qui se trouve à l’indice 1 du tableau trié.
console.log(uniqueNumbers[1]);
