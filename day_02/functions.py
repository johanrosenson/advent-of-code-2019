def process_input(input, noun, verb):

	input[1] = noun;
	input[2] = verb;

	next_instruction = 0

	while next_instruction < len(input):
		instruction = int(input[next_instruction])

		if instruction == 1 or instruction == 2:
			# addition or multiplication
			pos1 = int(input[next_instruction + 1])
			pos2 = int(input[next_instruction + 2])
			pos3 = int(input[next_instruction + 3])
			if instruction == 1:
				input[pos3] = int(input[pos1]) + int(input[pos2])
			elif instruction == 2:
				input[pos3] = int(input[pos1]) * int(input[pos2])
		elif instruction == 99:
			# print('Halt!')
			break
		else:
			print('Error! Unknown instruction: {}'.format(instruction))
			break

		next_instruction += 4

	return input[0]