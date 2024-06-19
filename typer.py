import sys
import math






def draw_cartouche(pos, line, draw): # pos; 0 is top, 1 is bottom
	bar = ''

	for j in range(accu_length[line], accu_length[line+1]):
		if (text[j][0] == ' /   '): 
			draw = True
			if (pos == 0): bar += '  ___'
			else:          bar += ' \\___'
		elif (text[j][0] == '\\    '):
			draw = False
			if (pos == 0): bar += '     '
			else:          bar += '/    '
		elif (draw):
			if (text[j][0] != 'SPACE   '):
				for m in range(len(text[j][0])): bar += '_'
		else:         
			if (text[j][0] != 'SPACE   '):
				for m in range(len(text[j][0])): bar += ' '

	print(bar)



text = []

# for every argument (word after the name of the program) that was given
# retrieve the file with that name, and add it to 'text' (without \n)
for i in range(1, len(sys.argv)):
	this_letter = []
	this_letter_file = open("/home/ondohir/programs/tp-ascii/words/" + sys.argv[i]) #there is probably a way to automate this :3    
	i = 0   																		#using ./ didn't work because when I was 
	for line in this_letter_file:													#somewhere else in the terminal it cried 
		this_letter.append(line.rstrip('\n'))
		i += 1
	text.append(this_letter)


# chop the text into lines
#   we run past every character and count the width up. When the total width of those characters
#   exceeds 100 (or whatever value is there), save the character at which the chop should be made,
#   and start over. Do this for every character

accu_length = [0]
current_length = 0
for i in range(len(text)):
	if(text[i][0] == 'SPACE   '):
		accu_length.append(i)
		current_length = 0
	else:
		current_length += len(text[i][0])
		if(current_length > 200): # the width of a line
			accu_length.append(i)
			current_length = len(text[i][0])
accu_length.append(len(text))


cartouche = False #

# runs through all the lines
for i in range(len(accu_length)-1):
	begin_with_cartouche = cartouche 
	drawn_cartouche = False
	if (cartouche):
		draw_cartouche(0, i, begin_with_cartouche)
		drawn_cartouche = True

	# then runs past every height line (the charactes are six ascii characters high)
	for j in range(6):
		this_line = ""

		# runs past all characters in this line
		for k in range(accu_length[i], accu_length[i+1]):


			# add that line for that character to the line that..
			#print(text[k][j])
			if(text[k][j] == 'SPACE   '):
				continue

			elif(text[k][0] == ' /   '): # left cartouche
				this_line += text[k][j]
				cartouche = True
				if ( not drawn_cartouche and j == 0 ): 
					draw_cartouche(0, i, begin_with_cartouche)
					drawn_cartouche = True

			elif (text[k][0] == '\\    '):
				this_line += text[k][j]
				cartouche = False


			else:
				this_line += text[k][j]
			#else: print("wow")

 		# ..we print right here
		print(this_line)

	if drawn_cartouche: # we only want a bottom cartouche if there's a top one
		draw_cartouche(1, i, begin_with_cartouche)



