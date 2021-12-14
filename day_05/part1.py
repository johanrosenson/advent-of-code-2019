# https://adventofcode.com/2019/day/5
from functions import process_instructions

instructions = [int(op) for op in open('input').read().split(',')]

# instructions = [int(op) for op in '3,9,8,9,10,9,4,9,99,-1,8'.split(',')]

input_value = 1

output = process_instructions(instructions, input_value)

print(output)