# LCS Algorithm

def LCS(string1, string2):
	str1Len = len(string1)
	str2Len = len(string2)

	lcsMatrix = [[0] * (str2Len + 1) for _ in range(str1Len + 1)] # LCS 2DArray

	#Running LCS to fill in the 2D array

	for i in range(1, str1Len + 1):
		for j in range(1, str2Len + 1):
			if string1[i - 1] == string2[j - 1]:
				lcsMatrix[i][j] = lcsMatrix[i - 1][j - 1] + 1
			else:
				lcsMatrix[i][j] = max(lcsMatrix[i - 1][j], lcsMatrix[i][j - 1])

	# Running TraceBack to determine actual LCS String

	lcsString = ''
	k = str1Len
	l = str2Len
	while k and l > 0:
		if string1[k - 1] == string2[l - 1]:
			lcsString += string1[k - 1]        # Doesn't matter if l or k is used
			k -= 1
			l -= 1
		elif lcsMatrix[k - 1][l] > lcsMatrix[k][l - 1]:
			k -= 1
		else:
			l -= 1
	lcsString = lcsString[::-1]   # The lscString is the lcs, but it does it backwards. This line reverses it

	return (lcsMatrix[str1Len][str2Len], lcsString)

# Code to read the file

file = open('CollectionSeqs/listSeqs-errorhigh-l50.txt')
stringList = list()
for line in file:
	stringList.append(line)

#Code to run the LCS Algorithm and produce an output

i = 0
printList = list()
while i < len(stringList):
	string1 = stringList[i]
	string2 = stringList[i+1]
	i += 2
	(length, string) = LCS(string1, string2)
	printList.append((length, string))

# Code to output answer

j = 0
for output in printList:
	outputTuple = printList[j]
	if outputTuple[0] == 0:
		print "There is no LCS of", stringList[j], "and", stringList[j + 1] 
	print "The length & LCS of", stringList[j], "and", stringList[j + 1], "is Length =", outputTuple[0], "and the LCS is", outputTuple[1], '\n'
	j += 1
