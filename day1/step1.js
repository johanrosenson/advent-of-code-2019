const fs = require('fs');

let input = fs.readFileSync('input', {encoding: 'utf8'}).split(/\r?\n/);

total_fuel = 0;

for (let n in input) {
	let fuel = Math.floor(input[n] / 3) - 2;
	while (fuel > 0) {
		total_fuel += fuel;
		fuel = Math.floor(fuel / 3) - 2;
	}
}

console.log(total_fuel);