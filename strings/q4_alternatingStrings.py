
# my approach - not correct; it produces correct answer but its not always minimum
def makeBeautiful(str):

	count = 0
	n = len(str)
	
	for i in range(1, n):

		if str[i] == str[i-1]:
			count += 1
			if str[i] == '0':
				str = str[:i] + '1' + str[i+1:]
			else:
				str = str[:i] + '0' + str[i+1:]

		else:
			continue

	return count


# optimal approach - produces correct result
def makeBeautiful(str):

	count1 = 0
	count2 = 0

	for i in range(len(str)):

		pos = i + 1

		if (pos % 2 == 1 and str[i] != '0') or (pos % 2 == 0 and str[i] != '1'):
			count1 += 1		
		
		if (pos % 2 == 1 and str[i] != '1') or (pos % 2 == 0 and str[i] != '0'):
			count2 += 1

	if count1 < count2:
		return count1

	return count1
	
