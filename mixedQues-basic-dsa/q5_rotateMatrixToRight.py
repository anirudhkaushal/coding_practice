from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

# brute force approach:
# time complexity: O(k*n*m)
# space complexity: O(1)
def rotateMatRight_(mat, n, m, k):
	
	for i in range(k):	
		for i in range(n):
			for j in range(m-1, 0, -1):
				mat[i][j], mat[i][j-1] = mat[i][j-1], mat[i][j]

	ans = []

	for i in range(n):
		for j in range(m):
			ans.append(mat[i][j])

	return ans


# optimal approach:
def rotateMatRight(mat, n, m, k):

	k = k % m

	for i in range(n):

		l = 0
		r = m - 1
		while l < r:
			mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
			l += 1
			r -= 1

		l = 0
		r = k - 1
		while l < r:
			mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
			l += 1
			r -= 1

		l = k
		r = m - 1
		while l < r:
			mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
			l += 1
			r -= 1

	ans = []
	for i in range(n):
		for j in range(m):
			ans.append(mat[i][j])

	return ans



# Taking the input.
def takeInput() :
	n, m, k = map(int, stdin.readline().strip().split(" "))
	mat = [list(map(int, stdin.readline().strip().split(" "))) for row in range(n)]
	return n, m, k, mat

# Printing the Matrix.
def printAns(ans):
	for i in ans:
		print(i, end = ' ')
	print('')

# Main.
t = int(input().strip())
for i in range(t):
	n, m, k, mat = takeInput()
	ans = rotateMatRight(mat, n, m, k)
	printAns(ans)