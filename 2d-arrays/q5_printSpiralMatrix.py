from sys import stdin

def spiralPrint(mat, nRows, mCols):
    
    ans = []

    top = 0
    left = 0
    right = mCols - 1
    bottom = nRows - 1

    while top <= bottom and left <= right:

        # right dir
        for i in range(left, right + 1):
            ans.append(mat[top][i])
        top += 1

        # bottom dir
        for i in range(top, bottom + 1):
            ans.append(mat[i][right])
        right -= 1

        # left dir
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(mat[bottom][i])
            bottom -= 1

        # top dir
        if left <= right:
        for i in range(bottom, top - 1, -1):
            ans.append(mat[i][left])
        left += 1


    for a in ans:
        print(a, end=" ")





























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1