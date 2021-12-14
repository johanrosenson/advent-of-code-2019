# https://adventofcode.com/2019/day/4
import re

[start, end] = [int(n) for n in open('input').read().split('-')]

passwords = []

for n in range(start, end+1):
	password = str(n)
	if re.match(r'.*(\d)\1', password) == None:
		continue

	if password != ''.join(sorted(password)):
		continue

	# print('valid: {}'.format(password))
	passwords.append(password)

print(len(passwords))