def getRow(rowIndex):
    if rowIndex == 0:
            return [1]
    if rowIndex == 1:
        return [1, 1]

    currRow = [1, 1]

    for i in range(rowIndex-1):

        tmpRow = [0] * (i + 3)
        n = len(tmpRow)

        for j in range(n):

            if j == 0 or j == n-1:
                tmpRow[j] = 1
            else:
                tmpRow[j] = currRow[j-1] + currRow[j]

        currRow = tmpRow

    return currRow

for i in range(6):
    print(getRow(i))
