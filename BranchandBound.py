def kurang(list):
    ct,kurang=0,0
    isikurang = [0 for i in range(16)]
    for i in list:
        for j in range(ct, len(list)):
            if i == 16 and (list.index(i) %2) == 0:
                kurang += 1
            if i > list[j]:
                isikurang[i-1] += 1
                kurang += 1
        ct+=1
    
    for i in range(len(isikurang)):
        print(f"Kurang({i+1}) = {isikurang[i]}")

    return kurang

def cost(list):
    patok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    cost = 0

    for i in range(len(list)):
        if list[i] != patok[i] and (list[i] != 16):
            cost += 1
    
    return cost

def beMatrix(list):
    matrix = [[0 for i in range(4)],[0 for i in range(4)],[0 for i in range(4)],[0 for i in range(4)]]
    for i in range(4):
        matrix[0][i]=list[i]
    for j in range(4,8):
        matrix[1][j-4]=list[j]
    for k in range(8,12):
        matrix[2][k-8]=list[k]
    for a in range(12,16):
        matrix[3][a-12]=list[a]
    return matrix



def getIndex(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 16:
                return i, j

def swapAtas(matriks):
    x,y = getIndex(matriks)
    matriks[x-1][y], matriks[x][y] = matriks[x][y], matriks[x-1][y]
    return matriks

def swapBawah(matriks):
    x,y = getIndex(matriks)
    matriks[x+1][y], matriks[x][y] = matriks[x][y], matriks[x+1][y]
    return matriks

def swapKanan(matriks):
    x,y = getIndex(matriks)
    matriks[x][y+1], matriks[x][y] = matriks[x][y], matriks[x][y+1]
    return matriks

def swapKiri(matriks):
    x,y = getIndex(matriks)
    matriks[x][y-1], matriks[x][y] = matriks[x][y], matriks[x][y-1]
    return matriks

class node:
    def __init__(self, parent, matrix, cost, blank, level):
        self.parent = parent
        self.matrix = matrix
        self.cost = cost
        self.blank = blank
        self.level = level
        
    def __lt__(self, other):
        if self.cost == other.cost:
            return self.level < other.level
        return self.cost < other.cost




