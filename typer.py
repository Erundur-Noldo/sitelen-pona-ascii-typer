import sys
import math

text = []

# for every argument (word after the name of the program) that was given
# retrieve the file with that name, and add it to 'text' (without \n)
for i in range(1, len(sys.argv)):
	this_letter = []
	this_letter_file = open("[your path]/tp-ascii/words/" + sys.argv[i]) #there is probably a way to automate this :3    
	i = 0   															 #using ./ didn't work because when I was 
	for line in this_letter_file:										 #somewhere else in the terminal it cried 
	this_letter.append(line.rstrip('\n'))
		i += 1
	text.append(this_letter)



# chops the text into groups of ten characters
for i in range( math.floor( len(text)/10 ) + 1):

	# then runs past every height line (the charactes are six ascii characters high)
	for j in range(6):
		this_line = ""

		# runs past the ten characters in this group
		for k in range(10):

			#if this one even exists
			if(10*i + k < len(text)):
				if( j < len(text[10*i+k]) ): 

					# add that line for that character to the line that..
					this_line += text[10*i+k][j]

		# ..we print right here
		print(this_line)
