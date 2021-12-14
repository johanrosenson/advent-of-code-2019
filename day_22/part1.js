require('../array');

console.time('part1');

const fs = require('fs');

const operations = fs.readFileSync('input.txt', 'utf8').trim()
    .split('\n')

const cards = 10007;

let deck = range(0, cards - 1);

for (operation of operations) {
    console.log(operation);
    if (operation === 'deal into new stack') {
        deck = deck.reverse();
    } else if (operation.startsWith('cut')) {
        const value = parseInt(operation.slice(4));

        const [cut, remaining] = [
            deck.slice(0, value),
            deck.slice(value),
        ];

        deck = remaining.concat(cut);
    } else if (operation.startsWith('deal with increment')) {
        const value = parseInt(operation.slice(20));

        const newDeck = (new Array(cards)).fill(null);

        let n = 0;

        while (typeof (card = deck.shift()) !== 'undefined') {
            newDeck[n] = card;

            // calculate next position
            n = (n + value) % cards;
        }

        deck = newDeck;
    } else {
        console.error('unsupported operation "' + operation + '"');
        break;
    }
}

// console.log({deck});

const position = deck.findIndex(card => card === 2019);

console.log(position);
