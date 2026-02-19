table = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]



# print(table)
# print(table[0])
# print(table[1])
# print(table[2])
# print(table[1][1])

# for row in table:
#     for value in row:
#         print(value, end=' ')
#     print()

for i in range(len(table)):
    for j in range(len(table[i])):
       table[i][j] *= 10



for i in range(len(table)):
    for j in range(len(table[i])):
        print(table[i][j], end=' ')
    print()