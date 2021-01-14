#_~-=%
def print_matrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end = " ")
        print()

def find_empty(mat):#_~-=%
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j] == ".":
                return i, j
    return None            

def valid(mat, num, pos):
    if num in mat[pos[0]]:
        return False
    for i in range(len(mat)):
        if mat[i][pos[1]] == num:
            return False
    a, b = pos[0] // 3 * 3, pos[1] // 3 * 3
    for i in range(a, a + 3):
        for j in range(b, b + 3):
            if mat[i][j] == num:
                return False
    return True            

def solve(mat):
    pos = find_empty(mat)
    if not pos:
        return True
    for num in range(1, 10):
        if valid(mat, num, pos):
            mat[pos[0]][pos[1]] = num
            if solve(mat):
                return True
            mat[pos[0]][pos[1]] = "."
    return False 

mat = [
    [7,8,'.',4,'.','.',1,2,'.'],
    [6,'.','.','.',7,5,'.','.',9],
    ['.','.','.',6,'.',1,'.',7,8],
    ['.','.',7,'.',4,'.',2,6,'.'],
    ['.','.',1,'.',5,'.',9,3,'.'],
    [9,'.',4,'.',6,'.','.','.',5],
    ['.',7,'.',3,'.','.','.',1,2],
    [1,2,'.','.','.',7,4,'.','.'],
    ['.',4,9,2,'.',6,'.','.',7]
]
print_matrix(mat)
print()
print()
print(solve(mat))
print()
print()
print_matrix(mat)


