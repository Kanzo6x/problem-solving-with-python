#https://codeforces.com/contest/768/problem/A
size = int(input())
arr = list(map(int,input().split()))
arr.sort()
counter = 0
if size == 1 or size == 2:
    print(0)
else:
    for i in range(1,size-1):
        if arr[i] > arr[0] and arr[i] < arr[-1]:
            counter += 1
    print(counter)