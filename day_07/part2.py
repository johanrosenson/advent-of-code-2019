# https://adventofcode.com/2019/day/7
from functions import process_instructions

instructions = [int(op) for op in open('input').read().split(',')]

instructions = [int(op) for op in '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'.split(',')]

stacks = {
	'input': [],
	'output': [],
}

def input_stack(value = None):
	# pop
	if value == None:
		value = stacks['input'].pop(0)
		# print('pop input {}'.format(value))
		return value

	# push
	# print('push input {}'.format(value))
	stacks['input'].append(value)

def output_stack(value = None):
	# pop
	if value == None:
		value = stacks['output'].pop()
		# print('pop output {}'.format(value))
		return value

	# push
	# print('push output {}'.format(value))
	stacks['output'].append(value)

	# also push to input stack
	input_stack(value)

def test_phase_settings(instructions, phase_settings):
	output = None

	# reset stacks
	stacks['input'] = []
	stacks['output'] = []

	for phase_setting in phase_settings:
		input_stack(phase_setting)
		input_stack((output, 0)[output == None])
		output = process_instructions(instructions, input_stack, output_stack)

	return output

def phase_settings_excluding(phase_settings, excluding):
	return phase_settings[0:phase_settings.index(excluding)] + phase_settings[phase_settings.index(excluding)+1:]

def generate_phase_settings(phase_settings, generated = []):
	for phase_setting in phase_settings:
		for sub_phase_setting in generate_phase_settings(phase_settings_excluding(phase_settings, phase_setting), []):
			generated.append([phase_setting] + sub_phase_setting)
	return ([phase_settings], generated)[len(generated) > 1]

highest_output = 0

# available_phase_settings = generate_phase_settings([0, 1, 2, 3, 4])
available_phase_settings = [[9,8,7,6,5]]

for phase_settings in available_phase_settings:
	output = test_phase_settings(instructions, phase_settings)
	if output > highest_output:
		highest_output = output

print('highest output: {}'.format(highest_output))
