array = []
for i in range(5):
    string = input()
    array2 = [int(x) for x in string.split()]
    array.append(array2)

for i in range(5):
    for j in range(5):
        if array[i][j] == 1:
            print(abs(i-2)+abs(j-2))
            break