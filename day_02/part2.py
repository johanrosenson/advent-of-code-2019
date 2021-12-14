# https://adventofcode.com/2019/day/2
from functions import process_input

input = open('input').read().split(',')

noun = 0
verb = 0

target = 19690720

print('Searching inputs for {}'.format(target))

while noun < 100:
	while verb < 100:
		output = process_input(input[:], noun, verb)

		if output == target:
			print('Input founds! Noun: {} Verb: {}'.format(noun, verb))
			print('Answer: {}'.format(noun * 100 + verb))
			exit()

		verb += 1
	noun += 1
	verb = 0

print('No matching input found!')
