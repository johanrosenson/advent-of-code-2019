def get_path(instructions):

	coord = {'x': 0, 'y': 0}
	path = {}

	total_steps = 0

	for instruction in instructions:
		[direction, steps] = [instruction[:1], instruction[1:]]

		axis = ('y', 'x')[direction in ['L', 'R']]
		axis_direction = (-1, 1)[direction in ['U', 'R']]

		for n in range(int(steps)):
			coord[axis] += axis_direction
			coord_key = '{}x{}'.format(coord['x'], coord['y'])
			total_steps += 1

			if path.get(coord_key) == None:
				path[coord_key] = {
					'distance': abs(coord['x']) + abs(coord['y']),
					# 'steps': [],
					'steps': total_steps,
				}

			# path[coord_key]['steps'].append(total_steps)

	return path

def shortest_distance_intersection(path1, path2):
	shortest_distance = None

	for coord in path1:
		if path2.get(coord) != None and (shortest_distance == None or path1[coord]['distance'] < shortest_distance):
			shortest_distance = path1[coord]['distance']

	return shortest_distance

def fewest_steps_intersection(path1, path2):
	fewest_steps = None

	for coord in path1:
		if path2.get(coord) != None:
			# steps = min(path1[coord]['steps']) + min(path2[coord]['steps'])
			steps = path1[coord]['steps'] + path2[coord]['steps']
			if fewest_steps == None or steps < fewest_steps:
				fewest_steps = steps

	return fewest_steps