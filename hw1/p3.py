import numpy as np

def rowOrder(mat, row, col):
    for i in range(row):
        for j in range(col):
            print(mat[i][j], end=' ')
    print()

def colOrder(mat, row, col):
    for i in range(col):
        for j in range(row):
            print(mat[j][i], end = ' ')
    print()

def spiralOrder(mat, row, col):
    top, bottom, left, right = 0, row - 1, 0, col - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(mat[top][i], end=' ')
        top += 1
        for i in range(top, bottom + 1):
            print(mat[i][right], end=' ')
        right -= 1
        if top <= bottom:
            for i in range (right, left - 1, -1):
                print(mat[bottom][i], end=' ')
            bottom -= 1
        if left <= right:
            for i in range (bottom, top - 1, -1):
                print(mat[i][left], end=' ')
            left += 1
    print()

def revSpiralOrder(mat, row, col):
    top, bottom, left, right = 0, row - 1, 0, col - 1
    while top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            print(mat[i][left], end=' ')
        left += 1
        
        for i in range (left, right + 1):
            print(mat[bottom][i], end=' ')
        bottom -= 1
        if left <= right:
            for i in range (bottom, top - 1, -1):
                print(mat[i][right], end=' ')
            right -= 1
        if top <= bottom:
            for i in range (right, left - 1, -1):
                print(mat[top][i], end=' ')
            top += 1
    print()

def diagOrder(mat, row, col):
    for j in range (col):
        x, y = 0, j
        while(x <= row - 1 and y >= 0):
            print(mat[x][y], end=' ')
            x += 1
            y -= 1
    for i in range (1, row):
        x, y = i, col - 1
        while(x <= row - 1 and y >= 0):
            print(mat[x][y], end=' ')
            x += 1
            y -= 1  
    print()     

def mirrorDiagOrder(mat, row, col):
    for j in range (col, -1, -1):
        x, y = 0, j
        while(x  <= row - 1 and y <= col - 1):
            print(mat[x][y], end=' ')
            x += 1
            y += 1
    for i in range (1, row):
        x, y = i, 0
        while(x  <= row - 1 and y <= col - 1):
            print(mat[x][y], end=' ')
            x +=1
            y +=1
    print()


row, col = input("Matrix dimensions? ").split()
row = int(row)
col = int(col)
matrix = np.random.randint(low = 1, high = 100, size = (row, col)) #generate matrix with random intergers
print("Initial matrix:")
print(matrix)
flag = True
while(flag):
    choice = input("Print order? ")
    choice = int(choice)
    if choice == 0:
        flag = False
    if choice == 1:
        rowOrder(matrix, row, col)
    if choice == 2:
        colOrder(matrix, row, col)
    if choice == 3:
        spiralOrder(matrix, row, col)
    if choice == 4:
        revSpiralOrder(matrix, row, col)
    if choice == 5:
        diagOrder(matrix, row, col)
    if choice == 6:
        mirrorDiagOrder(matrix, row, col)
        
