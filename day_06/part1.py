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

def count_transfers(orbit_map, orbit):
	count = 0
	while orbit_map.get(orbit) != None:
		count += 1
		orbit = orbit_map.get(orbit)
	return count

orbit_map = build_orbit_map(orbits)

orbit_count = count_orbits(orbit_map)

print(orbit_count)