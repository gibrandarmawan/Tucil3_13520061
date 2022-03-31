from tracemalloc import start
import numpy as np
import random
import BranchandBound as bnb


# startPuzzle = random.sample(range(0, 16), 16)
startPuzzle = [1,3,4,15,2,16,5,12,7,6,11,14,8,9,10,13]
# startPuzzle = [1,2,4,3,5,6,8,7,9,10,13,14,12,15,11,16]
# patok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

matrix = bnb.beMatrix(startPuzzle)
matrixnotswap = bnb.beMatrix(startPuzzle)
# print(startPuzzle)
# print(matrix)

matrix = bnb.swapKanan(matrix)

print(matrixnotswap)
print(matrix)

# print(matrixswapped)
# print(startPuzzle)
# kurang = bnb.kurang(startPuzzle)
