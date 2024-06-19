names = open('wordlist')
art_file = open('ascii-art')

art = []

for line in art_file:
	art.append(line.rstrip())

#making spaces
for i in range(8, 1365, 10): #1365 is the length of the ascii-art file
	length = 0
	for j in range(i, i+7):
		print(j)
		art[j] = art[j].rstrip()
		if( len(art[j]) > length): length = len(art[j])
	length += 3 #size of the space

	for j in range(i, i+6):
		while( len(art[j]) < length ):
			art[j] += ' '




#saving the files
i = -2
for line in names:
	i += 10
	file = open("./words/" + line.rstrip(), "w")
	for j in range(i, i+5):
		file.write(art[j] + '\n')
	file.write(art[i+5]) #last line without enter
	file.close

print("done")
