def SpiralOrder(matrix):
    List = []
    Size = len(matrix)
    try:
        for i in range(0, Size):
            for j1 in range(i, Size - i):
                List.append(matrix[i][j1])
            for j2 in range(i + 1, Size - i):
                List.append(matrix[j2][Size - i - 1])
            for j3 in range(Size - i - 2, i - 1, -1):
                List.append(matrix[Size - i - 1][j3])
            for j4 in range(Size - i - 2, i, -1):
                List.append(matrix[j4][i])
        return List
    except:
        return List
matrix = eval(input())
res = SpiralOrder(matrix)
print(res)