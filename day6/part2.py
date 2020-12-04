# https://adventofcode.com/2019/day/6

orbits = open('input').read().splitlines()

def build_orbit_map(orbits):
	orbit_map = {}
	for orbit in orbits:
		[a, b] = orbit.split(')')
		orbit_map[b] = a

	return orbit_map

def count_orbits(orbit_map):
	count = 0

	for orbit in orbit_map:
		count += count_transfers(orbit_map, orbit)

	return count

def get_path(orbit_map, node):
	path = []

	while orbit_map.get(node) != None:
		path.append(node)
		node = orbit_map.get(node)

	return path

def find_common(orbit_map, a, b):
	common = None

	ap = get_path(orbit_map, a)
	bp = get_path(orbit_map, b)

	for node in bp:
		if node in ap:
			common = node
			break

	return common

def count_transfers(orbit_map, orbit, target = None):
	count = 0
	while orbit_map.get(orbit) != None:
		count += 1
		orbit = orbit_map.get(orbit)
		if target != None and orbit == target:
			break
	return count

def count_transfers_between(orbit_map, a, b):
	count = 0
	common  = find_common(orbit_map, a, b)

	count += count_transfers(orbit_map, orbit_map['YOU'], common)
	count += count_transfers(orbit_map, orbit_map['SAN'], common)

	return count

orbit_map = build_orbit_map(orbits)

transfers = count_transfers_between(orbit_map, orbit_map['YOU'], orbit_map['SAN'])

print(transfers)