size = int(input())
string = input()
array_size = [int(i) for i in string.split()]
count = 0
police = 0
for i in range(size):
    if array_size[i] > 0:
        if array_size[i] > 10:
            police += 10
        else:
            police += array_size[i]
    elif array_size[i] == -1:
        if police > 0:
            police -= 1
        else:
            count += 1
print(count)