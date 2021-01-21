import numpy as np 

#_~-=%
def valid(arr, x, y):
    for i in range(y, -1, -1):
        if arr[x][i] == 1:
            return False

    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if arr[i][j] == 1:
            return False       

    for i, j in zip(range(x, n), range(y, -1, -1)):
        if arr[i][j] == 1:
            return False       
    return True

def solve(arr, y = 0):
    if y == n:
        return True
    for x in range(n):
        if valid(arr, x, y):
            arr[x][y] = 1
            if solve(arr, y + 1):
                return True
            arr[x][y] = 0
    return False        
         



n = int(input("Enter the size of matrix: "))
arr = np.zeros((n, n), dtype=int)
print(solve(arr))
print(arr)
