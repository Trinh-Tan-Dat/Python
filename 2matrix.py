matrix1 = [[1,2], [3,4]];
matrix2 = [[5,6], [7,8]];


result = [];
rows1 = len(matrix1);
cols2 = len(matrix2);
rows2 = len(matrix2);
cols1 = len(matrix1);

for i in range (rows1):
    result.append([0] * cols2)

print(result);

for i in range (rows1):
    for j in range (cols2):
        for k in range (cols1):
            result[i][j] += matrix1[i][k] + matrix2[k][j];

print(result)