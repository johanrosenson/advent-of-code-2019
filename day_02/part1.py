# https://adventofcode.com/2019/day/2
from functions import process_input

input = open('input').read().split(',')

# 1202 program alarm
output = process_input(input, 12, 2)

print(output)