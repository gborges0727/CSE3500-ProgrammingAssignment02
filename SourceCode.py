import timeit    # Used to calculate runtime below

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
	lcsString = lcsString[::-1]           # The lscString is the lcs, but it does it backwards. This line reverses it

	return (lcsMatrix[str1Len][str2Len] - 1, lcsString)      # -1 in return is needed to fix off by 1 error

# Code to read the file

file = open('CollectionSeqs/listSeqs-errorhigh-l10.txt')
stringList = list()
for line in file:
	stringList.append(line)

#Code to run the LCS Algorithm and produce an output

i = 1
startTime = timeit.default_timer()
for firstString in stringList:
	j = 1
	for secondString in stringList:
		if firstString == secondString:
			pass
		elif i > j:
			pass
		else:
			outputInfo = LCS(firstString, secondString)
			if outputInfo[0] != 0:
				k = len(firstString)
				l = len(secondString)
				average = (k + l) / 2.0
				normLCS = outputInfo[0] / average
				print "The LCS of strings", i, "and", j, "has a length of", outputInfo[0], "and the string:", outputInfo[1]
				#print normLCS
			else: 
				print "No LCS"
		j = j + 1
	i = i + 1
endTime = timeit.default_timer()
print "Runtime:", endTime - startTime, "seconds"
