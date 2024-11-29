#https://codeforces.com/contest/807/problem/A
n = int(input())
a, b = [], []
rated = False
maybe = True

for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
    if x != y:
        rated = True  

if rated:
    print("rated")
else:
    for i in range(1, n):
        if b[i] > b[i - 1]:  
            maybe = False
            break
    if maybe:
        print("maybe")
    else:
        print("unrated")
