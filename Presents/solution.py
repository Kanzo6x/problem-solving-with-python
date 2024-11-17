n = int(input())
string = input()
arr1= list(map(int,string.split()))
print(*[arr1.index(i+1)+1 for i in range(n)])