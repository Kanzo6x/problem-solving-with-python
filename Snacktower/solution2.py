#https://codeforces.com/problemset/problem/767/A
size_of_inputs = int(input())
arr = list(map(int, input().split()))
arr2 = set()  
maximam = size_of_inputs  

for snack in arr:
    arr2.add(snack)  
    while maximam in arr2:  
        print(maximam, end=" ")
        maximam -= 1  
    print()  

# time complexity is O(n)