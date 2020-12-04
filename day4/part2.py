# https://adventofcode.com/2019/day/4
import re

[start, end] = [int(n) for n in open('input').read().split('-')]

def is_valid(password):

	if password != ''.join(sorted(password)):
		return False

	if re.match(r'.*(\d)\1', password) == None:
		return False

	valid_group = False
	for group in re.findall(r'((\d)\2+)', password):
		if len(group[0]) == 2:
			valid_group = True

	if valid_group == False:
		return False

	return True

valid = 0

for n in range(start, end+1):
	password = str(n)
	if is_valid(password):
		valid += 1

print(valid)