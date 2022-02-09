Array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

sum = 0
row = len(Array)
col = len(Array[0])

for i in range(row):
    for j in range(col):
        sum += Array[i][j]
print(sum)
