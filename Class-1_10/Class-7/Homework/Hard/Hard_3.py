"""
    [*] Matrix Multiplication:
    Write a program to perform matrix multiplication. For the below matrices

    matrix_a = [
    1, 2, 3],
    [4, 5, 6] ]

	matrix_b = [
	[7, 8],
	[9, 10],
	[11, 12]
	]

"""
import numpy as np

matrix_a = [
	[1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
	[7, 8],
	[9, 10],
	[11, 12]
	]

result=[
	[0,0],
	[0,0]
]
for i in range(len(matrix_a)):
	for j in range(len(matrix_b[0])):
		for k in range(len(matrix_b)):
			result[i][j] += matrix_a[i][k] * matrix_b[k][j]

for r in result:
	print(result)