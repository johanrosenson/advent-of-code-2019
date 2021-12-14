import re

num_arguments = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}

def process_instructions(stack, input_value, pointer = 0):
	output_value = None
	while pointer < len(stack):
		[opcode, modes] = parse_op(stack[pointer])

		# print('opcode: {}'.format(opcode))

		if opcode == 99:
			return output_value

		# output_value = None
		next_pointer = None

		arguments = get_arguments(opcode, pointer, stack)

		if opcode == 1:
			op_add(arguments, stack, modes)
		elif opcode == 2:
			op_multiply(arguments, stack, modes)
		elif opcode == 3:
			op_input(arguments, stack, input_value)
		elif opcode == 4:
			output_value = op_output(arguments, stack, modes)
			# print('  debug output: {}'.format(output_value))
		elif opcode == 5:
			next_pointer = op_jump_true(arguments, stack, modes)
		elif opcode == 6:
			next_pointer = op_jump_false(arguments, stack, modes)
		elif opcode == 7:
			op_less(arguments, stack, modes)
		elif opcode == 8:
			op_equals(arguments, stack, modes)
		else:
			print('UNKNOWN OPCODE: "{}" ARGUMENTS: "{}" POINTER: "{}"'.format(opcode, arguments, pointer))
			exit()

		if next_pointer != None:
			pointer = next_pointer
		else:
			pointer += len(arguments)+1

	return output_value

def parse_op(op):
	[modes, opcode] = re.match(r'(.*?)?(.{1,2})$', str(op)).groups()

	if modes == None:
		modes = ''

	return [
		int(opcode), # trim leading zero
		[int(mode) for mode in list(modes[::-1])], # reverse and convert to array<int>
	]

def get_arguments(opcode, index, stack):
	if num_arguments.get(opcode) == None:
		return []

	return stack[index+1:index+num_arguments[opcode]+1]

def resolve_mode(index, modes, default_mode = 0):
	if index < len(modes):
		return modes[index]

	return default_mode

def resolve_argument(argument, stack, mode):
	if mode == 0:
		return stack[argument]
	elif mode == 1:
		return argument

def op_add(arguments, stack, modes):
	arguments[0] = resolve_argument(arguments[0], stack, resolve_mode(0, modes))
	arguments[1] = resolve_argument(arguments[1], stack, resolve_mode(1, modes))
	stack[arguments[2]] = arguments[0] + arguments[1]

def op_multiply(arguments, stack, modes):
	arguments[0] = resolve_argument(arguments[0], stack, resolve_mode(0, modes))
	arguments[1] = resolve_argument(arguments[1], stack, resolve_mode(1, modes))
	stack[arguments[2]] = arguments[0] * arguments[1]

def op_input(arguments, stack, input_value):
	stack[arguments[0]] = input_value

def op_output(arguments, stack, modes):
	return resolve_argument(arguments[0], stack, resolve_mode(0, modes))

def op_jump_true(arguments, stack, modes):
	arguments[0] = resolve_argument(arguments[0], stack, resolve_mode(0, modes))
	arguments[1] = resolve_argument(arguments[1], stack, resolve_mode(1, modes))
	if arguments[0] != 0:
		return arguments[1]

	return None

def op_jump_false(arguments, stack, modes):
	arguments[0] = resolve_argument(arguments[0], stack, resolve_mode(0, modes))
	arguments[1] = resolve_argument(arguments[1], stack, resolve_mode(1, modes))
	if arguments[0] == 0:
		return arguments[1]

	return None

def op_less(arguments, stack, modes):
	arguments[0] = resolve_argument(arguments[0], stack, resolve_mode(0, modes))
	arguments[1] = resolve_argument(arguments[1], stack, resolve_mode(1, modes))

	if arguments[0] < arguments[1]:
		stack[arguments[2]] = 1
	else:
		stack[arguments[2]] = 0

def op_equals(arguments, stack, modes):
	arguments[0] = resolve_argument(arguments[0], stack, resolve_mode(0, modes))
	arguments[1] = resolve_argument(arguments[1], stack, resolve_mode(1, modes))

	if arguments[0] == arguments[1]:
		stack[arguments[2]] = 1
	else:
		stack[arguments[2]] = 0