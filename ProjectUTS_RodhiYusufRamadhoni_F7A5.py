# ordo 2x3
mat1 = [
    [1, 0, 1],
    [1, 1, 0],
]

mat2 = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
]

mat3 = []

for b in range(0, len(mat1)):
    row = []
    for k in range(0, len(mat2[0])):
        result = 0
        for z in range(0, len(mat2)):
            result = result + (mat1[b][z] * mat2[z][k])
        row.append(result)
    mat3.append(row)


for b in range(0, len(mat3)):
    for k in range(0, len(mat2)):
        print (mat3[b][k], end=' ')
    print ()