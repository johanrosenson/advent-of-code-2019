# https://adventofcode.com/2019/day/7
from functions import process_instructions

instructions = [int(op) for op in open('input').read().split(',')]

# instructions = [int(op) for op in '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'.split(',')]

def test_phase_settings(instructions, phase_settings):
	output = None

	for phase_setting in phase_settings:
		output = process_instructions(instructions, [
			phase_setting,
			(output, 0)[output == None]
		])

	return output

def phase_settings_excluding(phase_settings, excluding):
	return phase_settings[0:phase_settings.index(excluding)] + phase_settings[phase_settings.index(excluding)+1:]

def generate_phase_settings(phase_settings, generated = []):
	for phase_setting in phase_settings:
		for sub_phase_setting in generate_phase_settings(phase_settings_excluding(phase_settings, phase_setting), []):
			generated.append([phase_setting] + sub_phase_setting)
	return ([phase_settings], generated)[len(generated) > 1]

highest_output = 0

for phase_settings in generate_phase_settings([0, 1, 2, 3, 4]):
	output = test_phase_settings(instructions, phase_settings)
	if output > highest_output:
		highest_output = output

print('highest output: {}'.format(highest_output))
