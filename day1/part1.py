# https://adventofcode.com/2019/day/1
import math

input = open('input').read().splitlines()

total_fuel_requirement = 0

for mass in input:
	fuel_requirement = math.floor(int(mass) / 3) - 2
	total_fuel_requirement += fuel_requirement

print("Total fuel requirement: {}".format(total_fuel_requirement))