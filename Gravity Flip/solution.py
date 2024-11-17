useless = int(input())
string = input()
array = [int(x) for x in string.split()]
array.sort()
print(*array)