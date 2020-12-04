# https://adventofcode.com/2019/day/3
from functions import get_path, fewest_steps_intersection

wires = open('input').read().splitlines()
paths = [{}, {}];

# wires = [
# 	'R8,U5,L5,D3',
# 	'U7,R6,D4,L4'
# ]

for wire in range(len(wires)):
	instructions = wires[wire].split(',')
	paths[wire] = get_path(instructions)

fewest_steps = fewest_steps_intersection(paths[0], paths[1])

print('Fewest steps: {}'.format(fewest_steps))