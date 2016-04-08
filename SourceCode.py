# LCS Algorithm

def LCS(string1, string2):
	return (1, "hello")

# Code to read the files

file = open('CollectionSeqs/listSeqs-errorlow-l50.txt')
stringList = list()
for line in file:
	stringList.append(line)

#Code to run through LCS Algorithm and produce an output

i = 0
printList = list()
while i < len(stringList):
	string1 = stringList[i]
	string2 = stringList[i+1]
	i += 2
	(length, string) = LCS(string1, string2)
	printList.append((length, string))

