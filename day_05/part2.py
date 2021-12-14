# https://adventofcode.com/2019/day/5
from functions import process_instructions
import sys

default_input_value = 0

instructions = [int(op) for op in open('input').read().split(',')]

# instructions = [int(op) for op in '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'.split(',')]

if len(sys.argv) > 1:
	input_value = int(sys.argv[1])
else:
	input_value = default_input_value

print('Input: {}'.format(input_value))

output_value = process_instructions(instructions, input_value)

print('Output: {}'.format(output_value))