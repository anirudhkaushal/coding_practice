
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

	
