#https://codeforces.com/problemset/problem/767/A
size_of_inputs = int(input())
string = input()
arr = list(map(int,string.split()))
arr2 = []
maximam = max(arr)
for i in range(size_of_inputs):
    if arr[i] is maximam:
        print(arr[i],end=" ")
        maximam-=1
        while maximam in arr2:
            print(arr2[-1],end=" ")
            arr2.pop()
            maximam-=1
        print()
    else:
        arr2.append(arr[i])
        arr2.sort()
        print()

#got a time limit exceed the time complexity was too big O(n^2 log n)