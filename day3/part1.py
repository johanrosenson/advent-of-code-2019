# https://adventofcode.com/2019/day/3
from functions import get_path, shortest_distance_intersection

wires = open('input').read().splitlines()
paths = [{}, {}];

for wire in range(len(wires)):
	instructions = wires[wire].split(',')
	paths[wire] = get_path(instructions)

shortest_distance = shortest_distance_intersection(paths[0], paths[1])

print('Shortest distance: {}'.format(shortest_distance))